# https://leetcode.com/problems/contains-duplicate/
# Note: True means has dupes, False means no dupes

# Solution 1: Seen-nums Hash-set Rolling Comparison
# Set is more space efficient than a dict since you only store keys and not values

def solution(input):
    seen_nums = set()
    for i in input:
        if i not in seen_nums:
            seen_nums.add(i)
        else:
            return True
    return False

# Solution 2: Set creation and len() comparison

# def solution(input):
#     test_set = set(input)
#     return len(input) != len(test_set)


# ==================================================================================================
# RUN TEST CASES
# ==================================================================================================
if __name__ == "__main__":
    test_cases = {
        ([], False),
        ([1], False),
        ([1, 1], True),
        ([1, 2], False),
        ([1, 1, 2], True),
        ([1, 3, 2], False),
        ([1, 4], False),
        ([1, 1, 2, 2], True),
    }

    for input, output in test_cases.items():
        print("====== BEGIN CASE:", input)
        if solution(input) != output:
            print("[FAIL]", "EXPECTED:", output)
        else:
            print("[PASS]")