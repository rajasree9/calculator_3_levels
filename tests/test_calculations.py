"""
This module contains tests for the calculator calculations module.

The tests are designed to verify the correctness of the Calculation class
and the history functionality provided by the Calculations class.
"""

from decimal import Decimal
import pytest  # Import pytest to use its fixtures
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract  # Import 'add' and 'subtract' functions

# Dummy test function
def test_dummy():
    """Test dummy function."""
    assert True

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3')

def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    add_operations = Calculations.find_by_operation("add")
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(add_operations) == 1 and len(subtract_operations) == 1

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None
