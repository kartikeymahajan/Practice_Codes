class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 2:
            return max(nums)
        else:
            li = []
            for i in range(0,2,1):
                count = 0
                for j in range(i,len(nums),2):
                    count += nums[j]
                li.append(count)
            return max(li)

nums = [1,2]
obj = Solution().rob(nums)
print(obj)