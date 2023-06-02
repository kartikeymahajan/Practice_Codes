'''20.Define sample code to achieve the following OOPs concepts

•Inheritance
•Method Overriding
•Encapsulation
•Method overloading
•Abstraction'''


# # Inheritance
# class Car():
#     def wheels(self):
#         print("Car have four wheels")
# class Creta(Car):
#     def info(self):
#         print("Creta is a Hyundai Car")

# obj = Creta()
# obj.wheels()

# # Method Overriding
# class Parent():
#     def show(self):
#         print("This is from parent class")

# class Child(Parent):
#     def show(self):
#         print("This is form child class")

# obj = Child()
# obj.show()

# Encapsulation

class Base:
    def __init__(self):
        self.a = "This is a"
        self.__c = "This is c"
 
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
# Driver code
obj1 = Base()
print(obj1.a)
print(obj1.__c)

# Method Overloading
# we can achive it by using multiple dispatch decorator.

from multipledispatch import dispatch
 
# passing one parameter
 
 
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)
 
# passing two parameters
 
 
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)
 
# you can also pass data type of any value as per requirement
 
 
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)
 
 
# calling product method with 2 arguments
product(2, 3)
 
# calling product method with 3 arguments but all int
product(2, 3, 2)
 
# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3)


# Abstraction
'''in python their is a term that is data hiding and we can achive it using __ before variable name
ex.  __myname = "kartikeya mahajan" '''




