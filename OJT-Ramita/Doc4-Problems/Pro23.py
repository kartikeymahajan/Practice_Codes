'''23.Write a logic for calculating the time taken for executing the python function'''

import time

now = time.time()

def add(n1, n2):
    return n1 + n2

obj = add(12,15)
print(obj)

print("Execution time taken:", time.time()-now)