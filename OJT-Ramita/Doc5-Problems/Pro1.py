'''1.Write a program in Python to find second highest number in an integer array without 
using inbuilt functions.'''

nums = [7,2,6,9,1,4,5]

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i]>nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print("Second Largest Element is",nums[-2])