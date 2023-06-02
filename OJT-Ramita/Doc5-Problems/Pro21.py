'''21.Write a program that takes one or more filenames as arguments and prints all the lines 
which are longer than 40 characters. 
Note :Use generator to solve this question.'''

def linesLongerThan40(file):
    f = open(file, "r")
    lines = f.readlines()
    for l in lines:
        if len(l)>40:
            yield l

obj = linesLongerThan40("Pro21File.txt")

for i in obj:
    print(i)
