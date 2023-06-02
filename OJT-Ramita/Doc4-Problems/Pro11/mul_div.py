def multiplication(f_value, *args):
    for i in args:
        f_value *= i
    return f_value

def division(f_value, *args):
    for i in args:
        f_value /= i 
    return round(f_value,1)

# mul = multiplication(2,2,2)
# print(mul)

# div = division(20,3)
# print(div)