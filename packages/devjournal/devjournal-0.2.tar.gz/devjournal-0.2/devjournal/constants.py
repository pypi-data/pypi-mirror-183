import os
from datetime import datetime
from pathlib import Path

TIME_FORMAT = "%Y-%m-%d_%H-%M-%S.%f"


def devjournal_dir():
    if directory := os.getenv("DEVJOURNAL_DIR"):
        return Path(directory)
    return Path.home() / ".devjournal"  # pragma: no cov


def config_file():
    return devjournal_dir() / "config.toml"


def entries_directory():
    return devjournal_dir() / "entries"


def filename_from_datetime(time: datetime):
    return f"{time.strftime(TIME_FORMAT)}.txt"


def datetime_from_filename(filename: str):
    return datetime.strptime(filename.replace(".txt", ""), TIME_FORMAT)
