def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return None
    if month == 2 and is_year_leap(year):
        return 29
    return days[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None
    total = 0
    for i in range(1, month):
        total += days_in_month(year, i)
    total += day
    return total

print(day_of_year(2000, 12, 31))