'''22. Write a function where month and year are taken as arguments which returns the output
with all the dates of saturdays occuring the month'''

from calendar import monthcalendar

def findSaturdays(month, year):
    d = monthcalendar(year,month)
    for i in d:
        if i[-2] != 0:
            yield (f'{i[-2]}/{month}/{year}')
    
obj = findSaturdays(3, 2023)

for i in obj:
    print(i)