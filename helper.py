from calendar import monthrange
import datetime

def date_check(month, day, year):
    date_now = datetime.datetime.now()
    current_year = date_now.year

    target_month = int(month)
    target_day = int(day)
    target_year = int(year)

    # Month Check
    if target_month > 12 or target_month < 1:
        return False

    # Day Check
    if target_day > 31 or target_day < 1:
        return False

    # Year Check
    if target_year > current_year or target_year < 1900:
        return False
    
    day_range = monthrange(target_year, target_month)

    # Valid days in the month check
    if target_day > day_range[1]:
        return False
    
    return True

    
