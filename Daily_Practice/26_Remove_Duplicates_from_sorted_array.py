
def removeDuplicates(nums: list[int]) -> int:
    size = len(nums)
    insertIndex = 1
    for i in range(1, size):
        # Found unique element
        if nums[i - 1] != nums[i]:      
            # Updating insertIndex in our main array
            nums[insertIndex] = nums[i] 
            # Incrementing insertIndex count by 1 
            insertIndex = insertIndex + 1       
    return insertIndex

nums = [2,4,2,5,6,3,1,4,2,6,7,3,2,7]
obj = removeDuplicates(nums)
print(obj)