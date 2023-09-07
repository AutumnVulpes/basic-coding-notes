# Bag Of Tools!!

## Hashmaps

- Aka a dictionary { }
- Lookup is constant time via hash function (to check if element exists, and what it stores)
- [Wiki article on hash maps](https://en.wikipedia.org/wiki/Hash_table)
- [Hash maps in python](https://www.geeksforgeeks.org/hash-map-in-python/)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)

Example:  
[002_majority_element.py](./solutions/002_majority_element.py)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}  # Empty dict of {num : index}

        for i, curr_num in enumerate(nums):  # For each index and number in nums:
            needed_num = target - curr_num

            if needed_num in seen_nums:  # Check if needed number was already seen
                return [i, seen_nums[needed_num]]

            seen_nums[curr_num] = i   # Otherwise, record that we saw it
```
