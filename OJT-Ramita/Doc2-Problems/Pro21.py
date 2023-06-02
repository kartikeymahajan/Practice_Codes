'''21. Write a callable called float_range that acts sort of like the built-in range callable
but it should allow for floating point numbers to be specified as start, stop, and
step values.

>>> r = float_range(0.5, 2.5, 0.5)
>>> r
float_range(0.5, 2.5, 0.5)
>>> list(r)
[0.5, 1.0, 1.5, 2.0]
>>> len(r)
4
>>> for n in r:
... print(n)
...
0.5
1.0
1.5
2.0'''

def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step


start = 0.5
stop = 3.5
step = 0.5

obj = float_range(start, stop, step)

print(list(obj))

for i in obj:
    print(i)


