var1 = 10
var2 = 20

print(f'Before swapping var1 = {var1} & var2 = {var2}')

var1 = var1 - var2
var2 = var1 + var2
var1 = var2 - var1

print(f'After swapping var1 = {var1} & var2 = {var2}')