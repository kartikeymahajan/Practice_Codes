'''20. Create a function that determines which day of the month the San Diego Python
meetup should be. It should accept year and month arguments and should return
a datetime.date object representing the day of the month for the meetup.
>>> meetup_date(2012, 3)
datetime.date(2012, 3, 22)'''

from datetime import datetime
import random

def takeDate(year, month):
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        date = random.randint(1,31)
    elif month in [4, 6, 9, 11]:
        date = random.randint(1,30)
    else:
        date = random.randint(1,28)
    
    temp = f'{year}, {month}, {date}'

    return datetime.strptime(temp, "%Y, %m, %d").date()

obj = takeDate(2024,2)
print(obj)
