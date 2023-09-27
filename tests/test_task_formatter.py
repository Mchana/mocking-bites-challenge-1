import pytest
from unittest.mock import Mock
from lib.task_formatter import TaskFormatter

def test_format_incomplete():
    task1 = Mock()
    task1.title = "bagel"
    task1.complete = False

    assert task1.format() == "- [ ] bagel"

def test_incomplete():
    task2 = Mock()
    task2.title = "hoovering"
    task2.complete = True

    assert task2.format() == "- [x] hoovering"
