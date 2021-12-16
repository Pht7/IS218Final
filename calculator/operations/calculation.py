"""Creating Calculation Class"""
class Calculation:
    def __init__(self, values: tuple):
        """Create constructor here"""
        self.values = Calculation.convert(values)
    """Only pass in first arg only"""
    @classmethod
    def create(cls,values: tuple):
        """Create objects, returning CLS"""
        return cls(values)
    @staticmethod
    def convert(values):
        """Make tuples into floats"""
        newFloat = []
        for x in values:
            newFloat.append(float(x))
        return tuple(newFloat)

