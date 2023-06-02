'''26. Write a function so that it accepts an iterable and returns True if the given iterable
is an iterator.'''


def is_itorator(iterable):
    return type(iter(iterable)) == type(iterable)

lis1 = [1, 2, 3, 4, 5]
temp = iter(lis1)
# print(type(lis1))

obj = is_itorator(temp)
print(obj)
