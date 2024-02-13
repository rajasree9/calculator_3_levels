from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Add two Decimal numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Subtract two Decimal numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Multiply two Decimal numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Divide two Decimal numbers. Raise ValueError if the divisor is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
