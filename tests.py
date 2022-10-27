import pytest

@pytest.fixture
def input_value():
   input = 2000
   return input

def test_Acceptance_criteria_1_leap_year(input_value):
    assert input_value % 4 == 0 and not input_value % 100 != 0

def test_Acceptance_criteria_2_leap_year(input_value):
    assert input_value % 400 == 0







