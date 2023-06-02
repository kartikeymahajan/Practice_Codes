'''30. Convert each list element to a key-value pair.
ex:
Input : test_list = [2323, 82, 129388, 95]
Output : {23: 23, 8: 2, 129: 388, 9: 5}'''


def convertToDict(li):
    output = {}
    for i in li:
        str_i = str(i)
        mid = len(str_i)//2
        output[int(str_i[:mid])] = int(str_i[mid:])
    return output

test_list = [2323, 82, 129388, 95]
obj = convertToDict(test_list)
print(obj)