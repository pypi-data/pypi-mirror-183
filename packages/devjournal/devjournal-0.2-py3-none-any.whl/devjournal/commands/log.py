import devjournal.entry
from devjournal.entry import get_entries


def log():
    devjournal.entry.print_entries(get_entries())
