def longestPalindrome(s: str) -> str: #type hinting
        dp = [[False]*len(s) for _ in range(len(s)) ]
        # print(dp)
        for i in range(len(s)):
            dp[i][i]=True
        ans=s[0]
        # print(dp)
        # print(ans)
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1): #Only executes whenever one of the "or" condition will true.
                    dp[i][j]=True
                    if j-i+1>len(ans):
                        ans=s[i:j+1]
        return ans

a = longestPalindrome('ada')
print(a)