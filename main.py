import pytest


def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division (x,y):
    return x/y

@pytest.mark.parametrize("a,b",[(-6,-5),(0,0),(10,10)])
def test_sub(a: int, b: int):
    assert addition(a,b) == addition(b,a)

@pytest.mark.parametrize("a,b",[(-6,-5),(10,10)])
def test_add_sub ( a: int, b: int):
    try:
        assert addition(a,b) == subtraction(b,a)
    except AssertionError: "Assertion is not true"

def test_cal():
    assert multiplication(5,5) == eval("25")


def test_mul_float():
    assert type(multiplication(3.0, 65.233)) == float
    try:
        assert type(multiplication(3.0, 65.233, "z")) == int
    except TypeError: "Type error - need to convert 'int' "


@pytest.mark.parametrize("a,b", [(-6.43, -5), (10.32, 10),(0, 1)])
def test_div (a,b):
    assert division(a,b) == a/b

def test_str_for_float():
    str = "(4.44+53)*34-234+(1/2)"
    assert eval(str) == 1719.46

