'''19. Write a program using decorators to print the traffic signal messages
Expected output -
RED : STOP
YELLOW : SLOW DOWN
GREEN : GO
The decorator should be working in this order'''

# defining a decorator
def hello_decorator(func):
 
    # inner1 is a Wrapper function in
    # which the argument is called
     
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("RED:STOP")
 
        # calling the actual function now
        # inside the wrapper function.
        func()
 
        print("GREEN:GO")
         
    return inner1
 
 
# defining a function, to be called inside wrapper
def function_to_be_used():
    print("YELLOW:SLOWDOWN")
 
 
# passing 'function_to_be_used' inside the
# decorator to control its behaviour
a = hello_decorator(function_to_be_used)
 
 
# calling the function
a()