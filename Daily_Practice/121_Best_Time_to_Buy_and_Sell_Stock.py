class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if(len(prices) == 0):
            return 0
        smallest = prices[0]
        max_profit = 0
        for elem in prices:
            if(elem < smallest):
                smallest = elem
            else:
                max_profit = max(max_profit, elem-smallest)
        return(max_profit)

prices = [5,3,6,2]
obj = Solution()
op = obj.maxProfit(prices)
print(op)