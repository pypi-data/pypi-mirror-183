from dataclasses import dataclass

import tomli
from rich import print

from devjournal.constants import config_file


@dataclass
class Config:
    remote_repo_url: str
    remote_branch: str

    @property
    def path(self):
        return str(config_file())

    def write(self):
        config_file().write_text(
            f'''remote_repo_url = "{self.remote_repo_url}"
remote_branch = "{self.remote_branch}"'''
        )
        print(f"Wrote config to {config_file()}.")


def get_config():
    if not config_file().exists():
        return Config("", "")
    config_dict = tomli.loads(config_file().read_text())
    return Config(**config_dict)
