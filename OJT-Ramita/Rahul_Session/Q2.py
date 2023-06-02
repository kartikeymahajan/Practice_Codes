data =  [[1,2,3], [], [], [[]], ["a"], ["a","b","c"], [[], "a"]]

def countEmptyList(data):
    count = 0
    for ele in data:
        if len(ele)== 0 or (type(ele[0])==list and len(ele[0])==0 and len(ele)==1):
            count += 1
    return count

obj = countEmptyList(data)
print(obj)