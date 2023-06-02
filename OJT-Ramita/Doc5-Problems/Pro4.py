'''4.Write Python program to perform left rotation of array elements by two positions.'''

arr = [10,20,30,40,50,60,70]
n = 2

# approach 1
# for i in range(n):
#     temp = arr[0]
#     arr.remove(temp)
#     arr.append(temp)
# print(arr)

# approach 2
arr = arr[n:] + arr[:n]
print(arr)


