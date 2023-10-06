# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_types = set(candyType)
        return min(len(unique_types), len(candyType) // 2)
        
        
        
# n-length int array for types
# at least 1 type, and can be duped up to n times, up to n unique types
# Find unique number of candy types -> use a set
# Constraint: n/2 candies

# Create a set of unique candy types
# Go through the input and add each one to the set
# Get length of the input array and divide by 2 to get the max number of candies Alice eats
# Get length of set of unique candy type
# Find the minimum between the 2 lengths, which should return max possible types eaten