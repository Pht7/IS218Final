"""testing addition"""
from calculator.operations.addition import Addition


def testing_addition():
    """testing calc result is 0"""
    assert Addition.add_number(1,2) == 3
