'''9. Create a function is_leap_year that accepts a year and returns True if (and only
if) the given year is a leap year.'''

def is_leap_year(year):
    return ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0))
    # return year % 4 == 0
    
obj = is_leap_year(1900)
print(obj)
        