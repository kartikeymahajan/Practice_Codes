import string

data = ["ANDAMAN", "GOA", "DELHI"]

def reverse(lst):
    for i in range(len(lst)):
        temp = ""
        if len(lst[i]) >= 5:
            for j in lst[i]:
                if j not in "aAeEiIoOuU":
                    temp += j
            lst[i] = temp[::-1]
            
    return lst

obj = reverse(data)
print(obj)