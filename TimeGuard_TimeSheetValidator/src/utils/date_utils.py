from dateutil.parser import parse

def is_same_day(date1, date2):
    return parse(date1).date() == parse(date2).date()