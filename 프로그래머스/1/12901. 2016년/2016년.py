import datetime

def solution(a, b):
    date_obj = datetime.date(2016, a, b)
    return date_obj.strftime('%a').upper()