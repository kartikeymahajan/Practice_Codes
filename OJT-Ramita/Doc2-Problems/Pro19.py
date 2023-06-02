'''19. Write a function that takes two strings representing dates and returns the string
that represents the earliest point in time ? Ex. get_earliest('01/27/1832',
'01/27/1756') return '01/27/1756' .   '''

from datetime import datetime as dt
def earliestDate(d1, d2):
    date1 = dt.strptime(d1, "%m/%d/%Y").date()
    date2 = dt.strptime(d2, "%m/%d/%Y").date()
    if date1 > date2:
        return d2
    else:
        return d1

d1 = '10/12/1832'
d2 = '01/27/1756'

# print(dt.strptime(d1, "%m/%d/%Y").date())

obj = earliestDate(d1, d2)
print(obj)