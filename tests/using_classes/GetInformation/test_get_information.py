import pytest
import os
import sys

from JSONManipulator import GetInformation


def test_get_information():
    # -- testing the class
    with pytest.raises(SystemExit) as e:
        GetInformation(
            desc="Categories", value="Java",
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        GetInformation(
            key="title", value="SBCD Exam Study Kit",  # mistake, but correlated by levenshtein
            levenshtein=0.7,
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        GetInformation(
            desc="Authors",
            value="W. Frank Aleson, Charlie Collins, Robi Sen",  # mistake, but correlated by levenshtein
            levenshtein=0.6,
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        GetInformation(
            desc="Title",
            value="Not found book",
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    assert e.value.code == 0