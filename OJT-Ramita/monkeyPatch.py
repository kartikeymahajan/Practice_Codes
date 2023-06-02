import test

def Cube(self, num):
    return f'The cube of {num} is {num**3}'

# Monkey Patching 
test.Power.square = Cube

obj = test.Power()
print(obj.square(3))