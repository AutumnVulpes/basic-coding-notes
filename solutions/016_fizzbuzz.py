# https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for num in range(1, n+1):
            if num % 15 == 0:
                res.append("FizzBuzz")
            elif num % 3 == 0:
                res.append("Fizz")
            elif num % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(num))
        
        return res
    
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         return['Fizz'*(i % 3 == 0) + 'Buzz'*(i % 5 == 0) or str(i) for i in range(1, n+1)]