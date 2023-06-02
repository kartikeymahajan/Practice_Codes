'''2. Write a decorator function that will record the number of times a function 
is called. Your decorator function should be called record_calls and call_count
attribute that keeps track of the number of times it was called.'''

def record_calls(func):
    call_count = 0
    for i in range(5):
        func()
        call_count+=1
    return call_count

def one_to_ten():
    print("Hello")

obj = record_calls(one_to_ten)
print(obj)

