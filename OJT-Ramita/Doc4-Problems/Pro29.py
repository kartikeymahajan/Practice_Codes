'''29.Find the element in a list using Binary Search Algorithm and return a tuple containing 
the element and its index.'''


def binary_search(arr, low, high, ele):
	
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == ele:
			return (ele, mid)
		elif arr[mid] > ele:
			return binary_search(arr, low, mid - 1, ele)
		else:
			return binary_search(arr, mid + 1, high, ele)
	else:
		return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

obj = binary_search(arr, 0, len(arr), x)
print(obj)


