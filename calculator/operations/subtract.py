"Creating an addition function"
from calculator.operations.calculation import Calculation
class Subtract(Calculation): # pylint: disable=too-few-public-methods
    """Create a subtract class"""
    def get_result(self):
        """Get total from subtract"""
        total = 0.0
        for value in self.values:
            total = total - value
        return total
