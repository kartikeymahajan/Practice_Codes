'''17.Define the function which returns the counts of saturdays part of a year 
(year is an input [Ex: 2022])'''

from datetime import date, timedelta

def all_sundays(year):
# January 1st of the given year
       dt = date(year, 1, 1)
    #    print(dt)
# First Sunday of the given year       
    #    print(dt.weekday())
       dt += timedelta(days = 11 - dt.weekday())  
       
       while dt.year == year:
          print(dt)
          dt += timedelta(days = 7)

all_sundays(2022)