"Creating an addition function"
from calculator.operations.calculation import Calculation
class Multiply(Calculation): # pylint: disable=too-few-public-methods
    """Create addition class"""
    def get_result(self):
        """Multiply results"""
        total = 1.0
        for value in self.values:
            total = total * value
        return total

