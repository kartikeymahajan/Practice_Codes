'''6. Write a function to_percent which accepts a number representing a ratio and
returns a string representing the percentage representation of the number to one
decimal place.'''

def to_percent(num):
    return f'{round(num,1)}%'

obj = to_percent(1/3)
print(obj)