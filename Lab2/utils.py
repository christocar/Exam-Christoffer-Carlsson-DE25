from numbers import Number

class Utils:
    """
    Validation for numeric numbers in this geometric lab.
    Made to control that it is a number is positive and non-zero.
    """
    @staticmethod
    def validate_number(value):
        """Raise TypeError if value is not a number."""
        if not isinstance(value, Number):
            raise TypeError(f"{value} is not a number.")

    @staticmethod
    def validate_positive(value):
        """Raise ValueError if value is not a positive non-zero number."""
        Utils.validate_number(value)
        if value <= 0:
            raise ValueError(f"{value} is not positive and non-zero.")