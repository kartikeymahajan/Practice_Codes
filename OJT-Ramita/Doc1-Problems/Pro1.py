'''1. Write a program to reverse a number without using any inbuit function.'''

def rev(num):
    st = str(num)
    return int(st[::-1])

obj = rev(578)
print(obj)
