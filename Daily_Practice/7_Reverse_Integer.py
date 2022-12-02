def reverseInteger(value:int) -> int:
    value = str(value)
    value = int(value[::-1])
    return value

op = reverseInteger(12534364)
print(op)