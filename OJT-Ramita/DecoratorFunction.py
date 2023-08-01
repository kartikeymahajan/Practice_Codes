'''Here we are modifying the behavior of hello function using decorator concept'''

def upper_case(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@upper_case # sending hello function to decorator funciton i.e.(upper_case()) equivalent to hello = upper_case(hello)
def hello(name, age):
    return f"Hello {name}, my age is {age}"

obj = hello("kiran", 34)
print(obj)

