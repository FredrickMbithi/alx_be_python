# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two values after validating them.
    Handles:
    - Non-numeric inputs
    - Division by zero
    """

    # Step 1: Convert to floats — catch non-numeric
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Step 2: Perform division — catch division by zero
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
