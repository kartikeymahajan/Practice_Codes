'''15. Given a list -- list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]
use the filter() function to find the list of numbers that are multiple of either 2 or 5.'''

list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]
result = list(filter(lambda x: x if x % 2 == 0 or x % 5 ==0 else False, list_1))
print(result)