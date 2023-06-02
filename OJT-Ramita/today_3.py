
inputt = [10, -2, 3, 4, 101, 200, 150, 97, 87, 87, 15]
result = [] 
final_op = [] 

def div_50(li):
    for i in li:
        if i % 50 == 0:
            result.append(i)
    return result

def div_3(li):
    for i in li:
        if i % 3 == 0:
            final_op.append(i)
    return final_op
    
obj = div_50(inputt)
obj1 = div_3(obj)
print(obj1)


