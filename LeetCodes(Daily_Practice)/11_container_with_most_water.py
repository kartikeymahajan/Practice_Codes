class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxx = 0 
        i = 0
        j = len(height)-1
        while i < j:
            width = abs(i-j)
            area = width * min(height[i],height[j])
            maxx = max(area,maxx)
            if height[i] > height[j]:
                j -=1
            else:
                i +=1
        return maxx 

h = [1,8,6,2,5,4,3,9]

obj = Solution()
print(obj.maxArea(h))