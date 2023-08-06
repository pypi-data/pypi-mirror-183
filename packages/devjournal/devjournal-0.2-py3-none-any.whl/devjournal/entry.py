from dataclasses import dataclass
from datetime import datetime

from rich import print
from rich.table import Table

from devjournal.constants import datetime_from_filename, entries_directory

TIME_FORMAT_FOR_PRINTING = "%Y-%m-%d %H:%M:%S"


@dataclass
class Entry:
    datetime: datetime
    text: str


def get_entries() -> list[Entry]:
    paths = entries_directory().glob("*.txt")
    return [
        Entry(datetime_from_filename(path.name), path.read_text()) for path in paths
    ]


def print_entries(entries: list[Entry]):
    for entry in entries:
        table = Table(show_header=False, show_lines=True, highlight=True)
        time = entry.datetime.strftime(TIME_FORMAT_FOR_PRINTING)
        table.add_row(f"{time}")
        table.add_row(f"{entry.text}")
        print(table)
