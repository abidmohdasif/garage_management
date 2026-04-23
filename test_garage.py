import pytest
from garage import calculate_fee

# garage1 = {
#     "capacity": 10,   # total number of spots
#     "cars": {}         # car_id -> entry_hour (int)
# }

# def test_enter_garage_new_car():
#     assert enter_garage(garage1, 12345, 2) ==

def test_calculate_fee():
    assert calculate_fee(3,2) == 6.00

def test_calculate_fee_Value_Error():
    with pytest.raises(ValueError):
        calculate_fee(-2,3)

def test_calculate_fee_Type_Error():
    with pytest.raises(TypeError):
        calculate_fee(hello,bye)
