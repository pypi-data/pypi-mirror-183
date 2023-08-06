import os
import subprocess
from datetime import datetime

from devjournal.constants import entries_directory, filename_from_datetime


def add(text: str | None = None):
    entries_directory().mkdir(parents=True, exist_ok=True)
    entry_file = entries_directory() / filename_from_datetime(datetime.now())
    if text:
        entry_file.write_text(text)
    else:
        _write_text_from_editor(entry_file)


def _write_text_from_editor(entry_file):
    entry_file.touch()
    command = [editor] if (editor := os.getenv("EDITOR")) else ["start", "/WAIT"]
    try:
        process = subprocess.Popen(
            command + [str(entry_file).replace("\\", "/")], shell=True
        )
        process.wait()
        text_in_file = entry_file.read_text()
        assert text_in_file
    except Exception:
        print("File empty, entry aborted.")
        entry_file.unlink()
