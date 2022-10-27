import pytest

@pytest.fixture
def input_value():
   input = 1999
   return input

def test_Acceptance_criteria_1__for_not_leap_year(input_value):
    assert input_value % 4 != 0

def test_Acceptance_criteria_2__for_not_leap_year(input_value):
    assert input_value % 100 != 0 and not input_value % 400 == 0


