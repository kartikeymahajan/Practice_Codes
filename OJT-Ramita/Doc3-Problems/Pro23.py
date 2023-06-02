'''23. Find the highest sum of the string by removing the duplicates for each iteration
input='1211' '''

def highest_sum(st:str):
    temp = 0
    st = set(st)
    for i in st:
        temp += int(i)
    new_st = str(temp)
    set_list = list(new_st)
    if set_list == list(set(set_list)):
        return new_st
    else :
        return highest_sum(new_st)

obj = highest_sum("2718789543669")
print(obj)