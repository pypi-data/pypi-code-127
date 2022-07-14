from typing import Optional
from dataclasses import dataclass
from subprocess import run, PIPE
from .exceptions import LoggedError


@dataclass
class Commit:
    sha: str
    first_parent: Optional[str] = None
    second_parent: Optional[str] = None

    @property
    def is_empty_merge(self) -> bool:
        """Check if commit is a merge that could have been fast-forward."""
        if self.first_parent and self.second_parent:
            # If the first parent is an ancestor of the second, then the head branch
            # was not behind the base branch by any commits, meaning a fast-forward was possible
            return _is_ancestor(self.first_parent, self.second_parent)

        # Not a merge
        return False


class DirtyWorkingTreeError(LoggedError):
    def __init__(self) -> None:
        super().__init__("Working tree is dirty.")


class NoRepoError(LoggedError):
    def __init__(self) -> None:
        super().__init__("Not a git repository or no remote 'origin' set.")


def ensure_repo() -> None:
    cmd = ["git", "remote", "get-url", "origin"]
    result = run(cmd, stdout=PIPE, stderr=PIPE)
    if result.returncode != 0:
        raise NoRepoError()


def ensure_clean_working_tree() -> None:
    cmd = ["git", "status", "--short"]
    result = run(cmd, stdout=PIPE, stderr=PIPE)
    output = result.stdout.decode().strip()
    if len(output) > 0:
        raise DirtyWorkingTreeError()


def get_head() -> Commit:
    """Get the head commit with its parent(s)"""
    cmd = ["git", "log", "--pretty=%h %p", "-n", "1"]
    result = run(cmd, stdout=PIPE)
    shas = result.stdout.decode().strip().split(" ")
    return Commit(*shas)


def get_repo_name() -> str:
    cmd = ["git", "remote", "get-url", "origin"]
    result = run(cmd, stdout=PIPE)
    url = result.stdout.decode().strip()
    name = url.split("/")[-1].split(".")[0]
    return name


def _is_ancestor(commit_a: str, commit_b: str) -> bool:
    """Checks if commit_a is an ancestor of commit_b"""
    cmd = ["git", "merge-head", "--is-ancestor", commit_a, commit_b]
    result = run(cmd, stdout=PIPE)
    return result.returncode == 0
