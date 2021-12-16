"""testing addition"""
from calculator.operations.subtract import Subtract

def testing_sub():
    """testing calc result is 0"""
    assert Subtract.sub_number(3,1) == 2
