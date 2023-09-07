#  https://leetcode.com/problems/majority-element/

# ==================================================================================================
# Hash Map Solution
# [Time: O(n) | Space: O(n)]
# ==================================================================================================

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         target = {}  # Create empty dictionary to store occurences
#         for n in nums:  # For each number in the list
#             if n not in target:  # Add occurence of new number
#                 target[n] = 1
#             else:  # Increment occurence of previously seen number by 1
#                 target[n] += 1
#             if target[n] > len(nums) / 2:  # Defined by questions as more than n/2
#                 return n


# ==================================================================================================
# Boyer-Moore Majority Voting Algorithm Solution
# [Time:  O(n) | Space: O(1)]
# ==================================================================================================

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_candidate = -1
        current_candidate_votes = 0

        for num in nums:
            if current_candidate_votes <= 0:
                current_candidate = num
                current_candidate_votes += 1
                continue
            
            if num == current_candidate:
                current_candidate_votes += 1
            else:
                current_candidate_votes -= 1

        return current_candidate