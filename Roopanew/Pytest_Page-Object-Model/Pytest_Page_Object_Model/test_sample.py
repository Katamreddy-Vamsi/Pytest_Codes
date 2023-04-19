def func(x):
    return x + 1


def test_answer():
    assert func(3) == 6 , "Run assert"

def method(x):
    return x + 1

def ans():
    assert method(4)==5 , "assert pass x y are same "
    assert method(5)==-1 , "assert failed"



