data = {"A":["Apple", "ANT"],
        "B":["Banana", "BAT"],
        "C":["Citrus", "CAT"]
        }

output = {}

def swapValueANdKeys(data):
    for ele in data:
        temp = data[ele]
        for i in temp:
            output[i] = ele
    return output

obj = swapValueANdKeys(data)
print(obj)