class Solution:
    # @return a list of lists of integers
    # 9:14
    def __init__(self):
        self.output = []

    def combine(self, n, k, pos=0, temp=None):
        temp = temp or []
        
        if len(temp) == k:
            self.output.append(temp[:])
            return

        for i in range(pos, n):
            temp.append(i+1)
            self.combine(n, k, i+1, temp)
            temp.pop()
        
        return self.output

obj = Solution()
op = obj.combine(5,3)
print(op)