# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Sliding Window Method
# Must slide with two pointers to find buy and sell point

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                if profit < prices[sell] - prices[buy]:
                    profit = prices[sell] - prices[buy]
            sell += 1
    
        return profit