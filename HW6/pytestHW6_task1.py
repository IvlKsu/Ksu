import HW6.class_task1 as task1


def test_get_created_instances():
    assert task1.User.get_created_instances() == 0


def test_instances_up():
    user, _, _ = task1.User(), task1.User(), task1.User()
    assert user.get_created_instances() == 3


def test_reset_instances_counter():
    user, _, _ = task1.User(), task1.User(), task1.User()
    assert user.reset_instances_counter() == 3














"""
def test_get_created_instances():
    assert User.get_created_instances() == 0
    
user = T1.User()

def test_instances_up():
    _, _, _ = T1.User(), T1.User(), T1.User()
    assert user.counter == 4


def test_instances_reset():
    user.reset_instances_counter()
    assert user.counter == 0
"""
