from pathlib import Path

import pytest
from pytest import MonkeyPatch

import devjournal.entry
import devjournal.git
from devjournal.entry import Entry


class MockPrintEntries:
    def __call__(self, entries: list[Entry]):
        self.entries = entries


class MockRepoReturner:
    def __init__(self) -> None:
        self.repo = MockRepo()

    def init(self, *args, **kwargs):
        return self.repo

    def __call__(self, *args, **kwargs):
        return self.repo


class MockRepo:
    class MockGit:
        def add(self, *args, **kwargs):
            pass

        def commit(self, *args, **kwargs):
            pass

        def push(self, *args, **kwargs):
            self.push_called = True

    class MockOrigin:
        def pull(self, *args, **kwargs):
            self.pull_called = True

    class MockHead:
        class MockReference:
            name = "myname"

        reference = MockReference

    def __init__(self, *args, **kwargs) -> None:
        self.git = self.MockGit()
        self.git.push_called = False
        self.origin = self.MockOrigin()
        self.origin.pull_called = False
        self.remotes = ["myremote"]
        self.head = self.MockHead

    def create_remote(self, *args, **kwargs):
        return self.origin

    def delete_remote(self, *args, **kwargs):
        pass


@pytest.fixture
def mock_repo(monkeypatch: MonkeyPatch):
    mock_repo_returner = MockRepoReturner()
    monkeypatch.setattr(devjournal.git, "Repo", mock_repo_returner)
    return mock_repo_returner.repo


@pytest.fixture(autouse=True)
def mock_devjournal_dir(monkeypatch: MonkeyPatch, tmp_path):
    monkeypatch.setenv("DEVJOURNAL_DIR", str(tmp_path))
    return tmp_path


@pytest.fixture()
def config_file(mock_devjournal_dir: Path):
    (mock_devjournal_dir / "config.toml").write_text(
        'remote_repo_url = "myrepo"\nremote_branch = "mybranch"'
    )


@pytest.fixture()
def mock_print_entries(monkeypatch: MonkeyPatch):

    return_value = MockPrintEntries()
    monkeypatch.setattr(devjournal.entry, "print_entries", return_value)

    return return_value
