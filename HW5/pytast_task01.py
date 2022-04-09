import pytest
from HW5.HW_task01 import Homework, Teacher, Student

expired_homework = Homework('calculate', 0)
oop_homework = Homework('read', 5)
student = Student('Roman', 'Petrov')
teacher = Teacher('Daniil', 'Ivanov')


def test_is_active():
    assert expired_homework.is_active() is False
    assert oop_homework.is_active() is True


def test_create_homework():
    assert teacher.create_homework("do something", 5).text == 'do something'


def test_do_homework():
    assert student.do_homework(expired_homework) is None
    assert student.do_homework(oop_homework) == oop_homework
