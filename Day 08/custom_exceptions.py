# Custom Exceptions
import traceback

class AppError(Exception):
    """Base class for all application-specific exceptions."""
    pass

class ValidationError(AppError):
    def __init__(self, message):
        super().__init__(message)

n = input("Enter a number: ")
try:
    if not n.isdigit():
        raise ValidationError("Input must be a valid number.")
    print("You entered a valid number:", n)

except ValidationError as ve:
    print("Validation Error:", ve)
    traceback.print_exc()
