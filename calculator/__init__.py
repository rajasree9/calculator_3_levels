from calculator.operations import add, subtract, multiply, divide

class SimpleCalculator:
    @staticmethod
    def add(a, b):
        return add(a, b)

    @staticmethod
    def subtract(a, b):
        return subtract(a, b)

    @staticmethod
    def multiply(a, b):
        return multiply(a, b)

    @staticmethod
    def divide(a, b):
        if b != 0:
            return divide(a, b)
        else:
            return "Cannot divide by zero"