class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        output = 0
        for i in grid:
            if i == grid[0]:
                for j in i:
                    output += j
            else:
                output += i[-1]
        return output


grid =  [[1,3,1],[1,5,1],[4,2,1]]
obj = Solution().minPathSum(grid)
print(obj)