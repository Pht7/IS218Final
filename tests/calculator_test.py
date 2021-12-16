"""Testing the Calculator"""
import pytest

from calculator.main import Calculator
from calculator.operations.addition import Addition
from calculator.operations.subtract import Subtract
from calculator.operations.multiply import Multiply
from calculator.operations.divison import Divison
from calculator.history.calculations import  Calculations
@pytest.fixture
def history_clear():
    """Calling a simple clear in here instead of referring to the other place"""
    Calculations.clear()
def test_add_static(history_clear):
    """Testing add static function"""
    add_tuple = (9.0, 3.0, 0.0)
    assert isinstance(Calculator.add_number(add_tuple), Addition)
    """This will add the numbers from tuple"""
    assert Calculations.last_item_value() == 12.0
def test_sub_static(history_clear):
    """Testing add static function"""
    sub_tuple = (9.0, 3.0, 0.0)
    assert isinstance(Calculator.subtract_number(sub_tuple), Subtract)
    """This will add the numbers from tuple"""
    assert Calculations.last_item_value() == -12.0
def test_multiply_static(history_clear):
    """Testing add static function"""
    multiply_tuple = (9.0, 3.0, 0.0)
    assert isinstance(Calculator.multiply_number(multiply_tuple), Multiply)
    """This will add the numbers from tuple"""
    assert Calculations.last_item_value() == -12.0
def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Addition.add_number(1,2) == 3

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Subtract.sub_number(3,2) == 1

def test_calculator_multiply():
    """Testing the subtract method of the calculator"""
    assert Multiply.multi(2,2) == 4
def test_calculator_divide():
    """Testing Divide method of calc"""
    assert Divison.divide(4,2) == 2
