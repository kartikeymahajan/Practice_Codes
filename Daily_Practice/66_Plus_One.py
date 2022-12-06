def PlusOne(digits:list [int])->list [int]:
    s = map(str, digits)
    i = int("".join(s))+1
    return list(map(int, list(str(i))))
d=[99]
op=PlusOne(d)
print(op)