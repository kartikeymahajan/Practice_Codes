# di = {}
# for l in li:
#     count = 1
#     while count <= len(li):
#         size = 0
#         for k in li:
#             if l == k:
#                 size +=1
#                 di[l]= size
#         count +=1

# l1 = di.keys()
# print(di)
# print(l1)

# def printTwoElements( arr, size):
#     for i in range(size):
#         if arr[abs(arr[i])-1] > 0:
#             arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
#         else:
#             print("The repeating element is ", abs(arr[i]))
             
#     for i in range(size):
#         if arr[i]>0:
#             print("and the missing element is ", i + 1)
 
# # Driver program to test above function */
# arr = [3,5,2,6,1]
# n = len(arr)
# printTwoElements(arr, n)

def missing_or_doubled(inputlist):
    counts = {}
    for n in inputlist:  # O(n) loop
        counts[n] = counts.get(n, 0) + 1
    print(counts)
    start = min(counts) 
    end = max(counts)
    # final O(n) loop to find missing number and number that appears twice
    # return [i for i in range(start, end + 1) if counts.get(i) in {2, None}]