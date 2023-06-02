'''13.Write a python program to take 2 inputs(numbers) from user. Divide the greater 
number by the smaller number. Validate the user inputs, it should be integer type only . 
If the input is not integer, raise exception and catch it. Also, if divisor is 0, 
catch the exception raised.'''

num1 = input()
num2 = input()
result = 0
try:
    num1 = int(num1)
    num2 = int(num2)
    try:
        if num1 > num2:
            result = num1/num2 
        else:
            result = num2/num1
        print(result)
    except:
        print("Zero Division Error")
except:
    print("Input should be int")