'''12.Write a Python Program to Reverse the Content of a File.

Input :-
I am
new to this 
world of 
Python.

Output :- 
Python. 
world of 
new to this 
I am'''

f = open("Pro12File.txt", "r")

data = f.readlines()

for i in range(len(data)-1, -1, -1):
    print(data[i])