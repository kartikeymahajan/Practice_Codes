'''18.Write sample code for reproducing the below errors and print the user defined 
messages with the use of exception handling concept

•IndexError,TypeError,AttributeError,ValueError'''

# IndexError
try:
    st = ["kartik", "sunny", "Hemant", "kunal"]
    print(st[4])    
except IndexError:
    print("IndexError: string st dosn't have given index")

# TypeError
try:
    a = "Msys"
    b = 2007
    print(a+b)
except TypeError:
    print("TypeError: You can't concate a int with string")

# AttributeError
try:
    num = 10
    num.append(15)
except AttributeError:
    print("AttributeError: int dosn't have append method")

#ValueError

try:
    st = 'msys'
    new = int(st)
    print(new)
except ValueError:
    print("ValueError: Invalid string literal to convert int()")
    