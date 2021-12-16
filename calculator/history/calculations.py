"""Calculation history Class"""
from calculator.operations.addition import Addition
from calculator.operations.subtract import Subtract
from calculator.operations.multiply import Multiply
class Calculations:
    """Create caculation classes for storing our history"""
    historyLS = []
    @staticmethod
    def clear():
        """Clear all items from our list"""
        Calculations.historyLS.clear()
        return True
    @staticmethod
    def count():
        """Get length"""
        return len(Calculations.historyLS)
    @staticmethod
    def last_item():
        """Get last item using index of -1"""
        return Calculations.historyLS[-1]
    @staticmethod
    def last_item_value():
        """Get last item value"""
        calc = Calculations.last_item()
        """Will call get result from other classes"""
        return calc.get_result()
    @staticmethod
    def first_item():
        """First item in index not value"""
        return Calculations.history[0]
    @staticmethod
    def get_calc(x):
        """Getting value x from index [0,x-1]"""
        return Calculations.historyLS[x]
    @staticmethod
    def add_calc(calc):
        """Call history"""
        return Calculations.historyLS.append(calc)
    @staticmethod
    def add_add_calc(values):
        """Stores addition function into history LS"""
        Calculations.add_calc(Addition.create(values))
        """Return result"""
        return Calculations.last_item_value()
    @staticmethod
    def add_sub_calc(values):
        """Stores addition function into history LS"""
        Calculations.add_calc(Subtract.create(values))
        """Return result"""
        return Calculations.last_item_value()
    @staticmethod
    def add_multi_calc(values):
        """Stores addition function into history LS"""
        Calculations.add_calc(Multiply.create(values))
        """Return result"""
        return Calculations.last_item_value()



