'''10.Generate a dictionary from the two given lists using diet function (without 
using for loops) and calculate the sum of all the values in the dictionary 
using reduce and anonymous concepts

L1 = ["a","b"]	L2 = [1,2]

Expected Output :

data = {"a":1, "b":2} 
sum = 3'''

import functools

L1 = ["a","b"]	
L2 = [1,2]

dictt = dict(zip(L1, L2))

print("data =",dictt)

s = functools.reduce(lambda a, b: a+b, dictt.values()) # reduce() works like map()

print("sum =", s)

