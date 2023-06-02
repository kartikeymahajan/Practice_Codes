'''19.Write a Python program to extract year, month, date and time using Lambda. I/p:
2020-01-15 09:03:32.744178

O/p :
Year : 2020
Month : 1
Day : 15
Time : 09:03:32.744178'''

import datetime

now = datetime.datetime.now()

func = lambda now: f"Year : {now.year}\nMonth : {now.month}\nDay : {now.day}\nTime : {now.time()}"

obj = func(now)
print(obj)
