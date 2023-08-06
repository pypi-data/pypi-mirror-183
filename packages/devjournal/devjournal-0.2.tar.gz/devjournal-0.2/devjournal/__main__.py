from typing import Optional

import typer

from .commands.add import add as add_command
from .commands.find import find as find_command
from .commands.log import log as log_command
from .commands.setup import setup as setup_command
from .git import is_repo_defined, pull_rebase, push

app = typer.Typer()


@app.command()
def setup():
    setup_command()


@app.command()
def add(text: Optional[list[str]] = typer.Argument(None)):
    if text:
        add_command(" ".join(text))
    else:
        add_command()
    if is_repo_defined():
        pull_rebase()
        push()


@app.command()
def log():
    if is_repo_defined():
        pull_rebase()
    log_command()


@app.command()
def find(words: list[str]):
    if is_repo_defined():
        pull_rebase()
    find_command(words)


if __name__ == "__main__":
    app()
