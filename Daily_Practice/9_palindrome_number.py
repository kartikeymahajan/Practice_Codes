class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        temp = int(temp[::-1])
        
        if temp == x:
            return True
        else:
            return False

obj = Solution()
op = obj.isPalindrome(11)
print(op)