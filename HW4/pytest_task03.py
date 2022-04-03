import sys
import HW4.HW4_task03 as task03


def test_task03():
    assert task03.my_precious_logger("error: file not found") in sys.stderr


def test_task03():
    assert task03.my_precious_logger("OK") in sys.stdout
