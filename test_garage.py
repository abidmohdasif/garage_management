import pytest
from garage import calculate_fee, enter_garage, exit_garage


def test_enter_garage_success():
    garage1 = {
    "capacity": 10,   # total number of spots
    "cars": {}         # car_id -> entry_hour (int)
    }
    enter_garage(garage1, 'BMW', 5)
    assert 'BMW' in garage1['cars'].keys()

def test_enter_garage_Type_Error():
    with pytest.raises(TypeError):
        enter_garage("garage1", 12345, "hello")

def test_enter_garage_full():
    with pytest.raises(ValueError):
        garage1 = {
        "capacity": 1,   # total number of spots
        "cars": {'BMW': 5}         # car_id -> entry_hour (int)
        }
        enter_garage(garage1, 'AUDI', 13)

def test_exit_garage_success():
        garage1 = {
        "capacity": 1,   # total number of spots
        "cars": {'BMW': 5}         # car_id -> entry_hour (int)
        }
        exit_garage(garage1, 'BMW')
        assert 'BMW' not in garage1['cars'].keys()

def test_exit_garage_Key_Error():
    with pytest.raises(KeyError):
        garage1 = {
        "capacity": 1,   # total number of spots
        "cars": {'BMW': 5}         # car_id -> entry_hour (int)
        }
        exit_garage(garage1, 'AUDI', 13)


def test_calculate_fee():
    assert calculate_fee(3,2) == 6.00

def test_calculate_fee_Value_Error():
    with pytest.raises(ValueError):
        calculate_fee(-2,3)

def test_calculate_fee_Type_Error():
    with pytest.raises(TypeError):
        calculate_fee("hello","bye")
