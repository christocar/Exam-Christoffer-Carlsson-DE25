from numbers import Number

class Utils:
    """
    Validation for numeric numbers in this geometric lab.
    Made to control that it is a number is positive and non-zero.
    """
    def validate_number(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"{value} is not a number.")

    def validate_positive(self, value):
        self.validate_number(value)
        if value <= 0:
            raise ValueError(f"{value} is not positive and non-zero.")