class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # n=len(prices)
        # max_profit=0
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         if prices[j] > prices[i]:
        #             p = prices[j]-prices[i]
        #             max_profit=max(max_profit,p)
        # return max_profit
        #2nd approach
        # min_price = float('inf')
        # max_profit = 0
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > max_profit:
        #         max_profit = price - min_price
                
        # return max_profit
        # 3rd approach
        min_price = float('inf')
        max_profit = 0
        n=len(prices)
        for i in range(0,n):
            min_price = min(prices[i],min_price)
            max_profit = max(max_profit,prices[i]-min_price)
        return max_profit