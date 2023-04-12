from main import *

def test_get_area():
    o = Rectangle(10, 10)
    assert o.get_area() == 100, "get area did not return expected value"

def test_set_width():
    o = Rectangle(10, 10)
    o.set_width(20)
    assert o.width == 20, "width did not set correctly"

def test_set_height():
    o = Rectangle(10, 10)
    o.set_height(20)
    assert o.height == 20, "height did not set correctly"