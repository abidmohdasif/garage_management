import pytest
from garage import calculate_fee, enter_garage

pytest.fixture
def garage {
    "cars": {}, # car_id -> entry_hour (int)
    "capacity": 10   # total number of spots        
}
def test_enter_garage_Type_Error():
    with pytest.raises(TypeError):
        enter_garage("garage1", 12345, "hello")

def test_enter_garage_success(garage):
    enter_garage(garage,12345,9)
    assert garage["cars"] == {12345 : 9}

def test_calculate_fee():
    assert calculate_fee(3,2) == 6.00

def test_calculate_fee_Value_Error():
    with pytest.raises(ValueError):
        calculate_fee(-2,3)

def test_calculate_fee_Type_Error():
    with pytest.raises(TypeError):
        calculate_fee("hello","bye")
