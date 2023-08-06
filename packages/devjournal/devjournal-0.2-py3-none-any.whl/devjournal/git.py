from git.repo import Repo

from devjournal.constants import entries_directory

from .config import get_config


def is_repo_defined():
    return bool(get_config().remote_repo_url)


def get_origin(remote_repo_url: str):
    repo = Repo.init(entries_directory())
    if repo.remotes:
        repo.delete_remote(repo.remotes[0])
    return repo.create_remote("origin", remote_repo_url)


def pull_rebase():
    remote_branch = get_config().remote_branch
    remote_repo_url = get_config().remote_repo_url
    get_origin(remote_repo_url).pull(rebase=True, refspec=remote_branch)


def push():
    remote_branch = get_config().remote_branch
    repo = Repo(entries_directory())
    repo.git.add(".")
    # TODO: change commit message here to time stamp or something
    repo.git.commit(message="devjournal commit")
    local_branch_name = repo.head.reference.name
    repo.git.push("--set-upstream", "origin", f"{local_branch_name}:{remote_branch}")
