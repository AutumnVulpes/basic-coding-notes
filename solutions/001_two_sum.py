# https://leetcode.com/problems/two-sum/description/

# ==================================================================================================
# O(n^2) Brute Force Solution
# ==================================================================================================

#class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

# ==================================================================================================
# O(n) Hash-map Solution
# ==================================================================================================

# While iterating over input list, popluate a hash map with seen numbers.
# At each step, the code knows target sum and current number
#
# Therefore, we can calculate the needed number and can just use the hash-map to check if it already
# exists and where it is position wise

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}  # Empty dict of {num : index}

        for i, curr_num in enumerate(nums):  # For each index and number in nums:
            needed_num = target - curr_num

            if needed_num in seen_nums:  # Check if needed number was already seen 
                return [i, seen_nums[needed_num]]

            seen_nums[curr_num] = i   # Otherwise, record that we saw it
