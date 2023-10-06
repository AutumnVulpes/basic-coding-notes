# https://leetcode.com/problems/coin-change-ii/description/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # # Initializing and setting up initial array
        # dp = [0] * (amount + 1)
        # dp[0] = 1
        
        # for coin in coins:
        #     for start_point in range(coin, amount + 1):
        #         dp[start_point] += dp[start_point - coin]

        # return dp[amount]
    
        dp = [([1] + [0] * (amount)) for _ in range(len(coins) + 1)]

        for i in range(1, len(coins) + 1):  # Previous attempts
            for value in range(1, amount + 1):
                if coins[i - 1] <= value:
                    dp[i][value] = dp[i][value - coins[i - 1]] + dp[i - 1][value]
                else:
                    dp[i][value] = dp[i - 1][value]

        return dp[-1][-1]