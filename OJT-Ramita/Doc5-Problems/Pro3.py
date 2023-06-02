'''3.Write Python Program to delete element from array at given index.'''

nums = [3,1,6,2,9,4,5]

# def delelement(arr, n):
#     for i in range(len(arr)):
#         if i == n:
#             arr = arr[:n] + arr[n+1:]
#     return arr

def delelement(arr, n):
    arr.pop(n)
    return arr

obj = delelement(nums, 5)
print(obj)



