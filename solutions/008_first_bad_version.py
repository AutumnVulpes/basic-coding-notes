# https://leetcode.com/problems/first-bad-version/description/

class Solution: 
    def binary_search(self, l, r, cond):
        while l < r:
            mid = l + (r - l) // 2
            if cond(mid):
                r = mid
            else:
                l = mid + 1
        return l

    def firstBadVersion(self, n: int) -> int:
        cond = isBadVersion
        res = self.binary_search(1, n, cond)  # Ask Brandon why not (0, n-1)
        return res