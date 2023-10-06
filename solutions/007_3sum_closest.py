# https://leetcode.com/problems/3sum-closest/

# res = set()
#     seen_nums = set()
#     input.sort()

#     for i, val in enumerate(input):
#         if val in seen_nums:
#             continue
#         seen_nums.add(val)
        
#         left = i + 1
#         right = (len(input)) - 1

#         while left < right:
#             triplet = val + input[left] + input[right]
#             if triplet < 0:
#                 left += 1
#             elif triplet > 0:
#                 right -= 1
#             else:
#                 res.add((val, input[left], input[right]))
#                 left += 1

#     return res

# nums.sort()
# print(nums)
# res = sum(nums[:3])

# for i in range(len(nums) - 2):
#     left = i + 1
#     right = len(nums) - 1

#     while left < right:
#         current = nums[i] + nums[left] + nums[right]
#         if current == target:
#             return target
#         elif abs(current - target) < abs(res - target):
#             res = current
#             print(f"{current} = {nums[i]} + {nums[left]} + {nums[right]}")  # Current & items check
#         elif current < target:
#             left += 1
#         else:
#             right -= 1

# return res

# Return the sum of the three integers closest to target
# Binary search setup
# Construct 2 pointers, if sum is too small, binary search to increase left, 
# if too big binary search to reduce left pointer

nums = [4,0,5,-5,3,3,0,-4,-5]

def binary_search(l, r, cond):
    while l < r:
        mid = l + (r - l) // 2  # Better than `(l + r) // 2` as it avoids overflow
        if cond(mid):
            r = mid
        else:
            l = mid + 1
    return l

nums.sort()

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)  # Start and end of list
        return binary_search(l, r, lambda i: target <= nums[i])
