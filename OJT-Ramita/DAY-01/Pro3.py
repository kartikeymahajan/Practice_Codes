'''3) Write a program to multiply two given number without using “*” operation or any in built 
function'''

def multiply(num1:int, num2:int)->int:
    op = 0
    for i in range(num2):
        op += num1
    return op

num1 = 6
num2 = 4

obj = multiply(num1, num2)
print(obj)