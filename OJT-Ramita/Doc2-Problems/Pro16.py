'''16. Write a function split_in_half that splits a list in half and returns both halves.
>>> split_in_half([1, 2, 3, 4])
([1, 2], [3, 4])'''

def split_in_half(li):
    mid_index = int((len(li)/2))
    return [li[:mid_index],li[mid_index:]]

li = [1, 2, 3, 4]
obj = split_in_half(li)
print(obj)