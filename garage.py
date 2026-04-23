def enter_garage(garage, car_id, entry_hour):
    pass

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    if hours < 0, or rate < 0:
        raise ValueError("hours or rate cannot be negative")
    return round(hours * rate, 2)
