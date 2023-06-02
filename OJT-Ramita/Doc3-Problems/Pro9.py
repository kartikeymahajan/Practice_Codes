'''9. Write a function swap_element that contains two args which will be the position of
elements present in the list. The function must swap the elements present in those
positions.
Input: [1,2,3,4,5,6,7,8] function: swap_element(arg1, arg2)'''

def swap_element(list, arg1, arg2):
    temp = list[arg1]
    list[arg1] = list[arg2]
    list[arg2] = temp
    return list

list = [1,2,3,4,5,6,7,8]
obj = swap_element(list, 2, 4)
print(obj)

