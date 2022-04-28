import pytest
import HW7.HW7_task4

storage = HW7.HW7_task4.KeyValueStorage('task_04.txt')


def test_check_task4():
   assert storage.name == 'kek\n'
   assert storage.song == 'shadilay\n'
   assert storage.power == '9001\n'
   assert storage.last_name == 'top\n'