# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def binary_search(self, l, r, cond):
        while l < r:
            mid = l + (r - l) // 2
            if cond(mid):
                r = mid
            else:
                l = mid + 1
        return l
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = self.binary_search(
            0, len(nums) - 1, lambda x: x < target)
        right = self.binary_search(
            0, len(nums) - 1, lambda x: x > target)
        if left > 0 and right > 0:
            return [left, right]
        print(left, right)
        return [-1, -1]

    
    
nums = [5,7,7,8,8,10]

class Solution:
    def binary_search(self, l, r, cond):
        while l < r:
            mid = l + (r - l) // 2
            print("Mid:", mid, "l:", l, "r:", r, cond(mid))
            if cond(mid):  # nums[x] >  (target - 1)
                r = mid - 1
            else:
                l = mid
        print(l, r)
        return l
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = self.binary_search(
            0, len(nums), lambda x: nums[x] >= target) - 1 
            # Use >= because it's the conjugate of <
        hi = self.binary_search(
            0, len(nums), lambda x: nums[x] >= target)
        if lo <= hi:
            return [lo, hi]
        return [-1, -1]

# low = last instance of number before target
# high = last instance of target