from src.app import add_num, sub_num


def test_add():
    assert add_num(3,4) == 7
    assert add_num(-5, 8) == 3

def test_sub():
    assert sub_num(5,3) == 2
    assert sub_num(-5,-2) == -3