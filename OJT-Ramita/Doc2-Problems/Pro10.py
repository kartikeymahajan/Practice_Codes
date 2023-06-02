'''10. Write a function combine_lists should take two lists and return a new list
containing all elements from both lists.'''

def combine_lists(li1,li2):
    return li1 + li2

li1 = [1,2,3,4,5]
li2 = [6,7,8,9,10]

obj = combine_lists(li1, li2)
print(obj)
