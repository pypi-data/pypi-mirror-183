from datetime import datetime

from pytest import CaptureFixture

from devjournal.entry import Entry, print_entries


def test_print_entries(capsys: CaptureFixture):
    print_entries([Entry(datetime(2022, 12, 26, 22, 55, 10), "hello world")] * 2)
    assert (
        capsys.readouterr().out
        == """┌─────────────────────┐
│ 2022-12-26 22:55:10 │
├─────────────────────┤
│ hello world         │
└─────────────────────┘
┌─────────────────────┐
│ 2022-12-26 22:55:10 │
├─────────────────────┤
│ hello world         │
└─────────────────────┘
"""
    )
