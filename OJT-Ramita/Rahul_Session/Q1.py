lst = [1, "23", 5, "Rahul", "xyz"]

def countStr(lst):
    counter = 0
    for i in lst:
        if type(i)==str:
            counter += 1
    return counter

obj = countStr(lst)
print(obj)

