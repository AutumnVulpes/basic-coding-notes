# https://leetcode.com/problems/fibonacci-number/description/

memo = {0:0, 1:1}

class Solution:

    def fib(self, n: int) -> int: 
        if n in memo:
            return memo[n]
        res = self.fib(n - 1) + self.fib(n - 2)
        memo[n] = res
        return res
            
        
        
        
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
#         return self.fib(n - 1) + self.fib(n - 2)
        
        
        
#         prev = 0
#         curr = 1
        
#         if n == 0:
#             return prev
#         if n == 1:
#             return curr
        
#         for i in range(2, n+1):
#             res = prev + curr
#             prev = curr
#             curr = res
#         return curr

            
            
        
# Input is integer
# Output is the number of fibonnaci sequence of said integer

# Edge Case: n = 0 or 1
# Working range 2 to n+1
# for loop 