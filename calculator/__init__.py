from decimal import Decimal
from typing import Callable

# Define arithmetic operations as functions
def add(a: Decimal, b: Decimal) -> Decimal:
    """Addition operation."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Subtraction operation."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Multiplication operation."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Division operation."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Define a function to perform a calculation
def perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
    """Perform a calculation."""
    return operation(a, b)

# Example usage
result_add = perform_operation(Decimal('5'), Decimal('3'), add)
result_subtract = perform_operation(Decimal('5'), Decimal('3'), subtract)
result_multiply = perform_operation(Decimal('5'), Decimal('3'), multiply)
result_divide = perform_operation(Decimal('5'), Decimal('3'), divide)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
