import devjournal.entry
from devjournal.entry import get_entries


def find(words: list[str]):
    entries = [
        entry for entry in get_entries() if any(word in entry.text for word in words)
    ]
    devjournal.entry.print_entries(entries)
