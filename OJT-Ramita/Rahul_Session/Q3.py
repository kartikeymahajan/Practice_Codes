data = [1,5,9,4,0,5]
data1 = (9,5,4,1,5,6)

def findSameData(data, data1):
    output = []
    for ele in data:
        if (ele in data1) and (ele not in output):
            output.append(ele)
    return output

def findDiffData(data, data1):
    output = []
    for ele in data:
        if ele not in data1:
            output.append(ele)
    return output


def findDiffUsingSet(d1, d2):
    d1 = set(d1)
    d2 = set(d2)
    inetersec = d1.intersection(d2)
    onlyInFirst = d1.difference(d2)
    onlyInSecond = d2.difference(d1)
    return onlyInSecond


obj3 = findDiffUsingSet(data, data1)
print(obj3)

# obj = findSameData(data, data1)
# print(obj)

# obj1 = findDiffData(data, data1)
# print(obj1)
