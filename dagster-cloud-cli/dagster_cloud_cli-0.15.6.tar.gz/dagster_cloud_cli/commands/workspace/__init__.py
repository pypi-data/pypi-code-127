import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import dagster._check as check
import yaml
from dagster.core.test_utils import remove_none_recursively
from dagster.serdes.serdes import deserialize_json_to_dagster_namedtuple
from dagster.utils import DEFAULT_WORKSPACE_YAML_FILENAME, frozendict
from dagster.utils.merger import deep_merge_dicts
from dagster_cloud_cli import gql, ui
from dagster_cloud_cli.config_utils import DEFAULT_AGENT_TIMEOUT, dagster_cloud_options
from dagster_cloud_cli.core.graphql_client import GqlShimClient
from dagster_cloud_cli.core.workspace import CodeDeploymentMetadata
from dagster_cloud_cli.utils import add_options, create_stub_command
from typer import Argument, Option, Typer

DEFAULT_LOCATIONS_YAML_FILENAME = "locations.yaml"

app = Typer(help="Manage your Dagster Cloud workspace.")

_DEPLOYMENT_METADATA_OPTIONS = {
    # Options to specify code location metadata inline
    "image": (str, Option(None, "--image", help="Docker image.")),
    "location_name": (str, Option(None, "--location-name", help="Location name.")),
    "python_file": (
        Path,
        Option(
            None, "--python-file", "-f", exists=False, help="Python file where repository lives."
        ),
    ),
    "working_directory": (
        str,
        Option(
            None,
            "--working-directory",
            "-d",
            help="Base directory to use for local imports when loading the repositories.",
        ),
    ),
    "package_name": (
        str,
        Option(
            None,
            "--package-name",
            "-p",
            help="Local or installed Python package where repositories live",
        ),
    ),
    "module_name": (
        str,
        Option(None, "--module-name", "-m", help="Python module where repositories live"),
    ),
    "executable_path": (
        str,
        Option(
            None,
            "--executable-path",
            help="Path to reach the executable to use for the Python environment to load the repositories. Defaults to the installed `dagster` command-line entry point.",
        ),
    ),
    "attribute": (
        str,
        Option(
            None,
            "--attribute",
            "-a",
            help=(
                "Optional attribute that is either a repository or a function that returns a repository."
            ),
        ),
    ),
    "commit_hash": (
        str,
        Option(
            None,
            "--commit-hash",
            help=(
                "Optional metadata which indicates the commit sha associated with this location."
            ),
        ),
    ),
    "git_url": (
        str,
        Option(
            None,
            "--git-url",
            help=(
                "Optional metadata which specifies a source code reference link for this location."
            ),
        ),
    ),
}

_LOCATION_FILE_OPTIONS = {
    # Specify code location metadata via file
    "location_file": (
        Path,
        Option(
            None,
            "--location-file",
            "--from",
            exists=True,
            help="YAML file specifying code location metadata.",
        ),
    ),
}


def _get_location_input(location: str, kwargs: Dict[str, Any]) -> gql.CliInputCodeLocation:
    python_file = kwargs.get("python_file")

    return gql.CliInputCodeLocation(
        name=location,
        python_file=str(python_file) if python_file else None,
        package_name=kwargs.get("package_name"),
        image=kwargs.get("image"),
        module_name=kwargs.get("module_name"),
        working_directory=kwargs.get("working_directory"),
        executable_path=kwargs.get("executable_path"),
        attribute=kwargs.get("attribute"),
        commit_hash=kwargs["git"].get("commit_hash")
        if "git" in kwargs
        else kwargs.get("commit_hash"),
        url=kwargs["git"].get("url") if "git" in kwargs else kwargs.get("git_url"),
    )


def _get_location_document(name: Optional[str], kwargs: Dict[str, Any]) -> Dict[str, Any]:

    name = name or kwargs.get("location_name")
    location_file = kwargs.get("location_file")

    location_doc_from_file = {}
    if location_file:
        with open(location_file, encoding="utf8") as f:
            location_doc_from_file = yaml.safe_load(f.read())

    if not location_file and not name:
        raise ui.error(
            "No location name provided. You must either provide a location file with the "
            f"{ui.as_code('--location-file/--from')} flag or specify the location name as an argument."
        )
    elif location_file:
        if "locations" in location_doc_from_file:
            if not name:
                raise ui.error(
                    "If specifying a file with multiple locations, must specify a location name."
                )
            locations_by_name = {l["location_name"]: l for l in location_doc_from_file["locations"]}
            if not name in locations_by_name:
                raise ui.error(f"No location with name {name} defined in location file.")
            location_doc_from_file = locations_by_name[name]
        elif (
            name
            and location_doc_from_file.get("location_name")
            and location_doc_from_file["location_name"] != name
        ):
            raise ui.error(
                f"Name provided via argument and in location file does not match, {name} =/= {location_doc_from_file['location_name']}."
            )

    python_file = kwargs.get("python_file")
    python_file_str = str(python_file) if python_file else None

    location_doc_from_kwargs = remove_none_recursively(
        {
            "location_name": name,
            "code_source": {
                "python_file": python_file_str,
                "module_name": kwargs.get("module_name"),
                "package_name": kwargs.get("package_name"),
            },
            "working_directory": kwargs.get("working_directory"),
            "image": kwargs.get("image"),
            "executable_path": kwargs.get("executable_path"),
            "attribute": kwargs.get("attribute"),
            "git": {"commit_hash": kwargs.get("commit_hash"), "url": kwargs.get("git_url")},
        }
    )
    return deep_merge_dicts(location_doc_from_file, location_doc_from_kwargs)


def _add_or_update_location(
    client: GqlShimClient, location_document: Dict[str, Any], agent_timeout: int
) -> None:
    try:
        gql.add_or_update_code_location(client, location_document)
        name = location_document["location_name"]
        ui.print(f"Added or updated location {name}.")
        wait_for_load(client, [name], agent_timeout)
    except Exception as e:
        raise ui.error(str(e))


@app.command(name="add-location", short_help="Add or update a repo location image.")
@dagster_cloud_options(allow_empty=True, requires_url=True)
@add_options(_DEPLOYMENT_METADATA_OPTIONS)
@add_options(_LOCATION_FILE_OPTIONS)
def add_command(
    api_token: str,
    url: str,
    agent_timeout: int,
    location: str = Argument(None, help="Code location name."),
    **kwargs,
):
    """Add or update the image for a repository location in the workspace."""
    with gql.graphql_client_from_url(url, api_token) as client:
        location_document = _get_location_document(location, kwargs)
        _add_or_update_location(client, location_document, agent_timeout)


def list_locations(location_names: List[str]) -> str:
    if len(location_names) == 0:
        return ""
    elif len(location_names) == 1:
        return location_names[0]
    else:
        return f"{', '.join(location_names[:-1])}, and {location_names[-1]}"


@app.command(name="update-location", short_help="Update a repo location image.")
@dagster_cloud_options(allow_empty=True, requires_url=True)
@add_options(_DEPLOYMENT_METADATA_OPTIONS)
@add_options(_LOCATION_FILE_OPTIONS)
def update_command(
    api_token: str,
    url: str,
    agent_timeout: int,
    location: str = Argument(None, help="Code location name."),
    **kwargs,
):
    """Update the image for a repository location in the workspace."""
    with gql.graphql_client_from_url(url, api_token) as client:
        location_document = _get_location_document(location, kwargs)
        _add_or_update_location(client, location_document, agent_timeout)


def wait_for_load(client, locations, timeout=DEFAULT_AGENT_TIMEOUT):
    try:
        agents = gql.fetch_agent_status(client)
    except Exception:
        raise ui.error("Unable to query agent status")
    if len(list(filter(lambda a: a["status"] == "RUNNING", agents))) == 0:
        ui.warn(
            f"No agents running, changes to {list_locations(locations)} will finish syncing once an agent starts."
        )
        return

    start_time = time.time()
    ui.print(f"Waiting for agent to sync changes to {list_locations(locations)}...")

    if not timeout:
        return

    while True:
        if time.time() - start_time > timeout:
            raise ui.error("Timed out waiting for location data to update.")

        try:
            nodes = gql.fetch_code_locations(client)
        except Exception as e:
            raise ui.error(str(e))

        nodes_by_location = {node["name"]: node for node in nodes}

        if all(
            location in nodes_by_location
            and nodes_by_location[location].get("loadStatus") == "LOADED"
            for location in locations
        ):

            error_locations = [
                location
                for location in locations
                if "locationOrLoadError" in nodes_by_location[location]
                and nodes_by_location[location]["locationOrLoadError"]["__typename"]
                == "PythonError"
            ]

            if error_locations:
                error_string = "Some locations failed to load after being synced by the agent:\n" + "\n".join(
                    [
                        f"Error loading {error_location}: {str(nodes_by_location[error_location]['locationOrLoadError'])}"
                        for error_location in error_locations
                    ]
                )
                raise ui.error(error_string)
            else:
                ui.print(
                    f"Agent synced changes to {list_locations(locations)}. Changes should now be visible in dagit."
                )
                break

        time.sleep(3)


@app.command(
    name="delete-location",
)
@dagster_cloud_options(allow_empty=True, requires_url=True)
def delete_command(
    api_token: str,
    url: str,
    location: str = Argument(..., help="Code location name."),
):
    """Delete a repository location from the workspace."""
    with gql.graphql_client_from_url(url, api_token) as client:
        try:
            gql.delete_code_location(client, location)
            ui.print(f"Deleted location {location}.")
        except Exception as e:
            raise ui.error(str(e))


@app.command(
    name="list",
)
@dagster_cloud_options(allow_empty=True, requires_url=True)
def list_command(
    url: str,
    api_token: str,
):
    """List repository locations in the workspace."""
    with gql.graphql_client_from_url(url, api_token) as client:
        execute_list_command(client)


def execute_list_command(client):
    list_res = gql.fetch_workspace_entries(client)

    ui.print("Listing locations...")

    for location in list_res:
        metadata = check.inst(
            deserialize_json_to_dagster_namedtuple(location["serializedDeploymentMetadata"]),
            CodeDeploymentMetadata,
        )

        location_desc = [location["locationName"]]
        if metadata.python_file:
            location_desc.append(f"File: {metadata.python_file}")
        if metadata.package_name:
            location_desc.append(f"Package: {metadata.package_name}")
        if metadata.image:
            location_desc.append(f"Image: {metadata.image}")

        ui.print("\t".join(location_desc))


@app.command(name="pull")
@dagster_cloud_options(allow_empty=True, requires_url=True)
def pull_command(
    url: str,
    api_token: str,
):
    """Retrieve code location definitions as a workspace.yaml file."""
    with gql.graphql_client_from_url(url, api_token) as client:
        document = gql.fetch_locations_as_document(client)
        ui.print_yaml(document or {})


@app.command(name="sync", short_help="Sync workspace with a workspace.yaml file.")
@dagster_cloud_options(allow_empty=True, requires_url=True)
def sync_command(
    url: str,
    api_token: str,
    agent_timeout: int,
    workspace: Path = Option(
        DEFAULT_WORKSPACE_YAML_FILENAME,
        "--workspace",
        "-w",
        exists=True,
        help="Path to workspace file.",
    ),
):
    """Sync the workspace with the contents of a workspace.yaml file."""
    with gql.graphql_client_from_url(url, api_token) as client:
        execute_sync_command(client, workspace, agent_timeout)


def format_workspace_config(workspace_config) -> Dict[str, Any]:
    """Ensures the input workspace config is in the modern format, migrating an input
    in the old format if need be."""
    check.dict_param(workspace_config, "workspace_config")

    if isinstance(workspace_config.get("locations"), (dict, frozendict)):
        # Convert legacy formatted locations to modern format
        updated_locations = []
        for name, location in workspace_config["locations"].items():
            new_location = {
                k: v
                for k, v in location.items()
                if k not in ("python_file", "package_name", "module_name")
            }
            new_location["code_source"] = {}
            if "python_file" in location:
                new_location["code_source"]["python_file"] = location["python_file"]
            if "package_name" in location:
                new_location["code_source"]["package_name"] = location["package_name"]
            if "module_name" in location:
                new_location["code_source"]["module_name"] = location["module_name"]

            new_location["location_name"] = name
            updated_locations.append(new_location)
        return {"locations": updated_locations}
    else:
        check.is_list(workspace_config.get("locations"))
        return workspace_config


def execute_sync_command(client, workspace, agent_timeout):
    with open(str(workspace), "r", encoding="utf8") as f:
        config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        processed_config = format_workspace_config(config)

    try:
        locations = gql.reconcile_code_locations(client, processed_config)
        ui.print(f"Synced locations: {', '.join(locations)}")
        wait_for_load(client, locations, agent_timeout)
    except Exception as e:
        raise ui.error(str(e))


try:
    from dagster_cloud.workspace.cli import snapshot_command

    app.command(name="snapshot", hidden=True)(snapshot_command)
except ImportError:
    app.command(name="snapshot", hidden=True)(create_stub_command("dagster-cloud"))
