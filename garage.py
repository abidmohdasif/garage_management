garage = {
    "capacity": 10,   # total number of spots
    "cars": {}         # car_id -> entry_hour (int)
}
def enter_garage(garage, car_id, entry_hour):
    if not isinstance(entry_hour, (int)):
        raise TypeError("entry_hour is not int")

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    if not isinstance(hours, (int,float)) or not isinstance(rate,(int,float)):
        raise TypeError("hours or rate is not int/float")
    if hours < 0 or rate < 0:
        raise ValueError("hours or rate cannot be negative")
    return round(hours * rate, 2)
