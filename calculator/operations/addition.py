"Creating an addition function"
from calculator.operations.calculation import Calculation
class Addition(Calculation): # pylint: disable=too-few-public-methods
    """Create addition class"""
    @staticmethod
    def get_add(self):
        """Total of results"""
        total = 0.0
        """Make a for loop to add all items in our list"""
        for value in self.values:
            total = value + total
        """After finishing loop of list, return sum"""
        return total

