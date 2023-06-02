# Case 1 - By Using O(N^2) Time Complexity
def findLenghtLongestSubarray(nums:list[int], target:int)->int:
	length = temp = 0
	for i in range(len(nums)):
		sum = 0
		for j in range(i, len(nums)):
			sum += nums[j]
			if sum == target:
				temp = len(nums[i:j+1])
				if temp > length:
					length = temp
	return length

# Case 2 - By Using O(n) Time Complexity
def findLenghtLongestSubarray1(nums:list[int], target:int)->int:
    di = {}
    sum = count = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum == target:
            count = i+1
        if sum in di:
            count = max(count, i-di[sum])
        else:
            di[sum] = i
    return count


# Case 3 -  Finding Local Minima
def findLocalMinima(arr:list[int], low:int, high:int)->int:
    # Finding index of middle element
    mid = low + (high - low) // 2
    size = len(arr)
 
    if(mid == 0 or arr[mid - 1] > arr[mid] and mid == size - 1 or arr[mid] < arr[mid + 1]):
        return arr[mid]
    elif(mid > 0 and arr[mid - 1] < arr[mid]):
        return findLocalMinima(arr, low, mid)
    else: 
        return findLocalMinima(arr, mid + 1, high)


# Driver Code
nums = [2, 2, 1, -3, 4, 3, 1, -8, 6, -2, -1]
target = 0
obj1 = findLenghtLongestSubarray(nums, target)
obj2 = findLenghtLongestSubarray1(nums, target)
obj3 = findLocalMinima(nums, 0, len(nums))
print("Case 1 Ans:", obj1)
print("Case 2 Ans:", obj2)
print("Case 3 Ans:", obj3)