# https://leetcode.com/problems/search-insert-position/


# Binary Search template
def binary_search(l, r, cond):
    while l < r:
        mid = l + (r - l) // 2  # Better than `(l + r) // 2` as it avoids overflow
        if cond(mid):
            r = mid
        else:
            l = mid + 1
    return l

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)  # Start and end of list
        return binary_search(l, r, lambda i: target <= nums[i])