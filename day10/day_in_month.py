def leap_year(leap):
    if leap % 4 == 0:
        if leap % 100 == 0:
            if leap % 400 == 0:
                return "leap year"
            else:
                return "not leap year"
        else:
            return "leap year"
    else:
        return "not leap year"
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and leap_year(year) == "leap year":
        return 29
    else:
        return month_days[month-1]
year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)