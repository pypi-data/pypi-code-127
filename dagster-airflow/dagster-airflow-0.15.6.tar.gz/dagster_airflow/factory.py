import datetime
import os
import re
from collections import namedtuple

from airflow import DAG
from airflow.models.baseoperator import BaseOperator
from dagster_airflow.operators.util import check_storage_specified

import dagster._check as check
import dagster.seven as seven
from dagster.core.definitions.reconstruct import ReconstructableRepository
from dagster.core.execution.api import create_execution_plan
from dagster.core.instance import DagsterInstance, is_dagster_home_set
from dagster.core.instance.ref import InstanceRef
from dagster.core.snap import ExecutionPlanSnapshot, PipelineSnapshot, snapshot_from_execution_plan
from dagster.utils.backcompat import canonicalize_backcompat_args

from .compile import coalesce_execution_steps
from .operators.docker_operator import DagsterDockerOperator
from .operators.python_operator import DagsterPythonOperator

DEFAULT_ARGS = {
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "owner": "airflow",
    "retries": 1,
    "retry_delay": datetime.timedelta(0, 300),
    "start_date": datetime.datetime(1900, 1, 1, 0, 0),
}

# Airflow DAG names are not allowed to be longer than 250 chars
AIRFLOW_MAX_DAG_NAME_LEN = 250


def _make_dag_description(pipeline_name):
    return """Editable scaffolding autogenerated by dagster-airflow from pipeline {pipeline_name}
    """.format(
        pipeline_name=pipeline_name
    )


def _rename_for_airflow(name):
    """Modify pipeline name for Airflow to meet constraints on DAG names:
    https://github.com/apache/airflow/blob/1.10.3/airflow/utils/helpers.py#L52-L63

    Here, we just substitute underscores for illegal characters to avoid imposing Airflow's
    constraints on our naming schemes.
    """
    return re.sub(r"[^\w\-\.]", "_", name)[:AIRFLOW_MAX_DAG_NAME_LEN]


class DagsterOperatorInvocationArgs(
    namedtuple(
        "DagsterOperatorInvocationArgs",
        "recon_repo pipeline_name run_config mode step_keys instance_ref pipeline_snapshot "
        "execution_plan_snapshot parent_pipeline_snapshot",
    )
):
    def __new__(
        cls,
        recon_repo,
        pipeline_name,
        run_config,
        mode,
        step_keys,
        instance_ref,
        pipeline_snapshot,
        execution_plan_snapshot,
        parent_pipeline_snapshot,
    ):
        return super(DagsterOperatorInvocationArgs, cls).__new__(
            cls,
            recon_repo=recon_repo,
            pipeline_name=pipeline_name,
            run_config=run_config,
            mode=mode,
            step_keys=step_keys,
            instance_ref=instance_ref,
            pipeline_snapshot=pipeline_snapshot,
            execution_plan_snapshot=execution_plan_snapshot,
            parent_pipeline_snapshot=parent_pipeline_snapshot,
        )


class DagsterOperatorParameters(
    namedtuple(
        "_DagsterOperatorParameters",
        (
            "recon_repo pipeline_name run_config "
            "mode task_id step_keys dag instance_ref op_kwargs pipeline_snapshot "
            "execution_plan_snapshot parent_pipeline_snapshot"
        ),
    )
):
    def __new__(
        cls,
        pipeline_name,
        task_id,
        recon_repo=None,
        run_config=None,
        mode=None,
        step_keys=None,
        dag=None,
        instance_ref=None,
        op_kwargs=None,
        pipeline_snapshot=None,
        execution_plan_snapshot=None,
        parent_pipeline_snapshot=None,
    ):
        pipeline_def = recon_repo.get_definition().get_pipeline(pipeline_name)

        if mode is None:
            mode = pipeline_def.get_default_mode_name()

        mode_def = pipeline_def.get_mode_definition(mode)

        check_storage_specified(pipeline_def, mode_def)

        return super(DagsterOperatorParameters, cls).__new__(
            cls,
            recon_repo=check.opt_inst_param(recon_repo, "recon_repo", ReconstructableRepository),
            pipeline_name=check.str_param(pipeline_name, "pipeline_name"),
            run_config=check.opt_dict_param(run_config, "run_config", key_type=str),
            mode=check.opt_str_param(mode, "mode"),
            task_id=check.str_param(task_id, "task_id"),
            step_keys=check.opt_list_param(step_keys, "step_keys", of_type=str),
            dag=check.opt_inst_param(dag, "dag", DAG),
            instance_ref=check.opt_inst_param(instance_ref, "instance_ref", InstanceRef),
            op_kwargs=check.opt_dict_param(op_kwargs.copy(), "op_kwargs", key_type=str),
            pipeline_snapshot=check.inst_param(
                pipeline_snapshot, "pipeline_snapshot", PipelineSnapshot
            ),
            execution_plan_snapshot=check.inst_param(
                execution_plan_snapshot, "execution_plan_snapshot", ExecutionPlanSnapshot
            ),
            parent_pipeline_snapshot=check.opt_inst_param(
                parent_pipeline_snapshot, "parent_pipeline_snapshot", PipelineSnapshot
            ),
        )

    @property
    def invocation_args(self):
        return DagsterOperatorInvocationArgs(
            recon_repo=self.recon_repo,
            pipeline_name=self.pipeline_name,
            run_config=self.run_config,
            mode=self.mode,
            step_keys=self.step_keys,
            instance_ref=self.instance_ref,
            pipeline_snapshot=self.pipeline_snapshot,
            execution_plan_snapshot=self.execution_plan_snapshot,
            parent_pipeline_snapshot=self.parent_pipeline_snapshot,
        )


def _make_airflow_dag(
    recon_repo,
    job_name,
    run_config=None,
    mode=None,
    instance=None,
    dag_id=None,
    dag_description=None,
    dag_kwargs=None,
    op_kwargs=None,
    operator=DagsterPythonOperator,
):
    check.inst_param(recon_repo, "recon_repo", ReconstructableRepository)
    check.str_param(job_name, "job_name")
    run_config = check.opt_dict_param(run_config, "run_config", key_type=str)
    mode = check.opt_str_param(mode, "mode")
    # Default to use the (persistent) system temp directory rather than a TemporaryDirectory,
    # which would not be consistent between Airflow task invocations.

    if instance is None:
        if is_dagster_home_set():
            instance = DagsterInstance.get()
        else:
            instance = DagsterInstance.local_temp(tempdir=seven.get_system_temp_directory())

    check.inst_param(instance, "instance", DagsterInstance)

    # Only used for Airflow; internally we continue to use pipeline.name
    dag_id = check.opt_str_param(dag_id, "dag_id", _rename_for_airflow(job_name))

    dag_description = check.opt_str_param(
        dag_description, "dag_description", _make_dag_description(job_name)
    )
    check.class_param(operator, "operator", superclass=BaseOperator)

    dag_kwargs = dict(
        {"default_args": DEFAULT_ARGS},
        **check.opt_dict_param(dag_kwargs, "dag_kwargs", key_type=str),
    )

    op_kwargs = check.opt_dict_param(op_kwargs, "op_kwargs", key_type=str)

    dag = DAG(dag_id=dag_id, description=dag_description, **dag_kwargs)
    pipeline = recon_repo.get_definition().get_pipeline(job_name)

    if mode is None:
        mode = pipeline.get_default_mode_name()

    execution_plan = create_execution_plan(pipeline, run_config, mode=mode)

    tasks = {}

    coalesced_plan = coalesce_execution_steps(execution_plan)

    for solid_handle, solid_steps in coalesced_plan.items():
        step_keys = [step.key for step in solid_steps]

        operator_parameters = DagsterOperatorParameters(
            recon_repo=recon_repo,
            pipeline_name=job_name,
            run_config=run_config,
            mode=mode,
            task_id=solid_handle,
            step_keys=step_keys,
            dag=dag,
            instance_ref=instance.get_ref(),
            op_kwargs=op_kwargs,
            pipeline_snapshot=pipeline.get_pipeline_snapshot(),
            execution_plan_snapshot=snapshot_from_execution_plan(
                execution_plan, pipeline_snapshot_id=pipeline.get_pipeline_snapshot_id()
            ),
        )
        task = operator(operator_parameters)

        tasks[solid_handle] = task

        for solid_step in solid_steps:
            for step_input in solid_step.step_inputs:
                for key in step_input.dependency_keys:
                    prev_solid_handle = execution_plan.get_step_by_key(key).solid_handle.to_string()
                    if solid_handle != prev_solid_handle:
                        tasks[prev_solid_handle].set_downstream(task)

    return (dag, [tasks[solid_handle] for solid_handle in coalesced_plan.keys()])


def make_airflow_dag(
    module_name,
    job_name,
    run_config=None,
    mode=None,
    instance=None,
    dag_id=None,
    dag_description=None,
    dag_kwargs=None,
    op_kwargs=None,
    pipeline_name=None,
):
    """Construct an Airflow DAG corresponding to a given Dagster job/pipeline.

    Tasks in the resulting DAG will execute the Dagster logic they encapsulate as a Python
    callable, run by an underlying :py:class:`PythonOperator <airflow:PythonOperator>`. As a
    consequence, both dagster, any Python dependencies required by your solid logic, and the module
    containing your pipeline definition must be available in the Python environment within which
    your Airflow tasks execute. If you cannot install requirements into this environment, or you
    are looking for a containerized solution to provide better isolation, see instead
    :py:func:`make_airflow_dag_containerized`.

    This function should be invoked in an Airflow DAG definition file, such as that created by an
    invocation of the dagster-airflow scaffold CLI tool.

    Args:
        module_name (str): The name of the importable module in which the pipeline/job definition can be
            found.
        job_name (str): The name of the job definition.
        run_config (Optional[dict]): The config, if any, with which to compile
            the pipeline/job to an execution plan, as a Python dict.
        mode (Optional[str]): The mode in which to execute the pipeline.
        instance (Optional[DagsterInstance]): The Dagster instance to use to execute the pipeline/job.
        dag_id (Optional[str]): The id to use for the compiled Airflow DAG (passed through to
            :py:class:`DAG <airflow:airflow.models.DAG>`).
        dag_description (Optional[str]): The description to use for the compiled Airflow DAG
            (passed through to :py:class:`DAG <airflow:airflow.models.DAG>`)
        dag_kwargs (Optional[dict]): Any additional kwargs to pass to the Airflow
            :py:class:`DAG <airflow:airflow.models.DAG>` constructor, including ``default_args``.
        op_kwargs (Optional[dict]): Any additional kwargs to pass to the underlying Airflow
            operator (a subclass of
            :py:class:`PythonOperator <airflow:airflow.operators.python_operator.PythonOperator>`).
        pipeline_name (str): (legacy) The name of the pipeline definition.

    Returns:
        (airflow.models.DAG, List[airflow.models.BaseOperator]): The generated Airflow DAG, and a
        list of its constituent tasks.

    """
    check.str_param(module_name, "module_name")
    job_name = canonicalize_backcompat_args(
        new_val=job_name,
        new_arg="job_name",
        old_val=pipeline_name,
        old_arg="pipeline_name",
        breaking_version="future versions",
        coerce_old_to_new=lambda val: val,
    )

    recon_repo = ReconstructableRepository.for_module(module_name, job_name, os.getcwd())
    return _make_airflow_dag(
        recon_repo=recon_repo,
        job_name=job_name,
        run_config=run_config,
        mode=mode,
        instance=instance,
        dag_id=dag_id,
        dag_description=dag_description,
        dag_kwargs=dag_kwargs,
        op_kwargs=op_kwargs,
    )


def make_airflow_dag_for_operator(
    recon_repo,
    job_name,
    operator,
    run_config=None,
    mode=None,
    dag_id=None,
    dag_description=None,
    dag_kwargs=None,
    op_kwargs=None,
    pipeline_name=None,
):
    """Construct an Airflow DAG corresponding to a given Dagster job/pipeline and custom operator.

    `Custom operator template <https://github.com/dagster-io/dagster/blob/master/python_modules/dagster-test/dagster_test/dagster_airflow/custom_operator.py>`_

    Tasks in the resulting DAG will execute the Dagster logic they encapsulate run by the given
    Operator :py:class:`BaseOperator <airflow.models.BaseOperator>`. If you
    are looking for a containerized solution to provide better isolation, see instead
    :py:func:`make_airflow_dag_containerized`.

    This function should be invoked in an Airflow DAG definition file, such as that created by an
    invocation of the dagster-airflow scaffold CLI tool.

    Args:
        recon_repo (:class:`dagster.ReconstructableRepository`): reference to a Dagster RepositoryDefinition
            that can be reconstructed in another process
        job_name (str): The name of the job definition.
        operator (type): The operator to use. Must be a class that inherits from
            :py:class:`BaseOperator <airflow.models.BaseOperator>`
        run_config (Optional[dict]): The config, if any, with which to compile
            the pipeline to an execution plan, as a Python dict.
        mode (Optional[str]): The mode in which to execute the pipeline.
        instance (Optional[DagsterInstance]): The Dagster instance to use to execute the pipeline.
        dag_id (Optional[str]): The id to use for the compiled Airflow DAG (passed through to
            :py:class:`DAG <airflow:airflow.models.DAG>`).
        dag_description (Optional[str]): The description to use for the compiled Airflow DAG
            (passed through to :py:class:`DAG <airflow:airflow.models.DAG>`)
        dag_kwargs (Optional[dict]): Any additional kwargs to pass to the Airflow
            :py:class:`DAG <airflow:airflow.models.DAG>` constructor, including ``default_args``.
        op_kwargs (Optional[dict]): Any additional kwargs to pass to the underlying Airflow
            operator.
        pipeline_name (str): (legacy) The name of the pipeline definition.

    Returns:
        (airflow.models.DAG, List[airflow.models.BaseOperator]): The generated Airflow DAG, and a
        list of its constituent tasks.
    """
    check.class_param(operator, "operator", superclass=BaseOperator)

    job_name = canonicalize_backcompat_args(
        new_val=job_name,
        new_arg="job_name",
        old_val=pipeline_name,
        old_arg="pipeline_name",
        breaking_version="future versions",
        coerce_old_to_new=lambda val: val,
    )

    return _make_airflow_dag(
        recon_repo=recon_repo,
        job_name=job_name,
        run_config=run_config,
        mode=mode,
        dag_id=dag_id,
        dag_description=dag_description,
        dag_kwargs=dag_kwargs,
        op_kwargs=op_kwargs,
        operator=operator,
    )


def make_airflow_dag_for_recon_repo(
    recon_repo,
    job_name,
    run_config=None,
    mode=None,
    dag_id=None,
    dag_description=None,
    dag_kwargs=None,
    op_kwargs=None,
    pipeline_name=None,
):
    job_name = canonicalize_backcompat_args(
        new_val=job_name,
        new_arg="job_name",
        old_val=pipeline_name,
        old_arg="pipeline_name",
        breaking_version="future versions",
        coerce_old_to_new=lambda val: val,
    )
    return _make_airflow_dag(
        recon_repo=recon_repo,
        job_name=job_name,
        run_config=run_config,
        mode=mode,
        dag_id=dag_id,
        dag_description=dag_description,
        dag_kwargs=dag_kwargs,
        op_kwargs=op_kwargs,
    )


def make_airflow_dag_containerized(
    module_name,
    job_name,
    image,
    run_config=None,
    mode=None,
    dag_id=None,
    dag_description=None,
    dag_kwargs=None,
    op_kwargs=None,
    pipeline_name=None,
):
    """Construct a containerized Airflow DAG corresponding to a given Dagster job/pipeline.

    Tasks in the resulting DAG will execute the Dagster logic they encapsulate  using a subclass of
    :py:class:`DockerOperator <airflow:airflow.operators.docker_operator.DockerOperator>`. As a
    consequence, both dagster, any Python dependencies required by your solid logic, and the module
    containing your pipeline definition must be available in the container spun up by this operator.
    Typically you'll want to install these requirements onto the image you're using.

    This function should be invoked in an Airflow DAG definition file, such as that created by an
    invocation of the dagster-airflow scaffold CLI tool.

    Args:
        module_name (str): The name of the importable module in which the pipeline/job definition can be
            found.
        job_name (str): The name of the job definition.
        image (str): The name of the Docker image to use for execution (passed through to
            :py:class:`DockerOperator <airflow:airflow.operators.docker_operator.DockerOperator>`).
        run_config (Optional[dict]): The config, if any, with which to compile
            the pipeline/job to an execution plan, as a Python dict.
        mode (Optional[str]): The mode in which to execute the pipeline.
        dag_id (Optional[str]): The id to use for the compiled Airflow DAG (passed through to
            :py:class:`DAG <airflow:airflow.models.DAG>`).
        dag_description (Optional[str]): The description to use for the compiled Airflow DAG
            (passed through to :py:class:`DAG <airflow:airflow.models.DAG>`)
        dag_kwargs (Optional[dict]): Any additional kwargs to pass to the Airflow
            :py:class:`DAG <airflow:airflow.models.DAG>` constructor, including ``default_args``.
        op_kwargs (Optional[dict]): Any additional kwargs to pass to the underlying Airflow
            operator (a subclass of
            :py:class:`DockerOperator <airflow:airflow.operators.docker_operator.DockerOperator>`).
        pipeline_name (str): (legacy) The name of the pipeline definition.

    Returns:
        (airflow.models.DAG, List[airflow.models.BaseOperator]): The generated Airflow DAG, and a
        list of its constituent tasks.
    """
    check.str_param(module_name, "module_name")
    check.str_param(job_name, "job_name")
    check.str_param(image, "image")
    check.opt_dict_param(run_config, "run_config")
    check.opt_str_param(mode, "mode")
    check.opt_str_param(dag_id, "dag_id")
    check.opt_str_param(dag_description, "dag_description")
    check.opt_dict_param(dag_kwargs, "dag_kwargs")
    check.opt_dict_param(op_kwargs, "op_kwargs")

    job_name = canonicalize_backcompat_args(
        new_val=job_name,
        new_arg="job_name",
        old_val=pipeline_name,
        old_arg="pipeline_name",
        breaking_version="future versions",
        coerce_old_to_new=lambda val: val,
    )
    recon_repo = ReconstructableRepository.for_module(module_name, job_name, os.getcwd())

    op_kwargs = check.opt_dict_param(op_kwargs, "op_kwargs", key_type=str)
    op_kwargs["image"] = image

    return _make_airflow_dag(
        recon_repo=recon_repo,
        job_name=job_name,
        run_config=run_config,
        mode=mode,
        dag_id=dag_id,
        dag_description=dag_description,
        dag_kwargs=dag_kwargs,
        op_kwargs=op_kwargs,
        operator=DagsterDockerOperator,
    )


def make_airflow_dag_containerized_for_recon_repo(
    recon_repo,
    job_name,
    image,
    run_config=None,
    mode=None,
    dag_id=None,
    dag_description=None,
    dag_kwargs=None,
    op_kwargs=None,
    instance=None,
    pipeline_name=None,
):
    check.inst_param(recon_repo, "recon_repo", ReconstructableRepository)
    check.str_param(job_name, "job_name")
    check.str_param(image, "image")
    check.opt_dict_param(run_config, "run_config")
    check.opt_str_param(mode, "mode")
    check.opt_str_param(dag_id, "dag_id")
    check.opt_str_param(dag_description, "dag_description")
    check.opt_dict_param(dag_kwargs, "dag_kwargs")
    op_kwargs = check.opt_dict_param(op_kwargs, "op_kwargs", key_type=str)
    check.opt_str_param(pipeline_name, "pipeline_name")

    op_kwargs["image"] = image

    job_name = canonicalize_backcompat_args(
        new_val=job_name,
        new_arg="job_name",
        old_val=pipeline_name,
        old_arg="pipeline_name",
        breaking_version="future versions",
        coerce_old_to_new=lambda val: val,
    )
    return _make_airflow_dag(
        recon_repo=recon_repo,
        job_name=job_name,
        run_config=run_config,
        mode=mode,
        dag_id=dag_id,
        dag_description=dag_description,
        dag_kwargs=dag_kwargs,
        op_kwargs=op_kwargs,
        operator=DagsterDockerOperator,
        instance=instance,
    )
