class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n_nums = len(nums)
        total = sum(nums)
        if abs(target) > total:
            return 0    
        
        dp = [[0 for _ in range(total * 2 + 1)] for i in range(n_nums)]
        dp[0][0] = 1

        for row in range(1, n_nums + 1):  # row is index + 1
            for col in range(total * 2 + 1):  # col is current sum
                if nums[row] <= col:
                    dp[row][col] = dp[row - 1][col] + dp[row - 1][col - nums[row - 1]]
                else:
                    dp[row][col] = dp[row - 1][col]
        
        return dp [-1][-1]