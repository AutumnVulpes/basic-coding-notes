# https://leetcode.com/problems/3sum/description/

# Psuedocode funtime rambling
# res = []
# sort input (by ascending)
# Iterate through input via enum for the first number 
# and use two pointer method for other two numbers
#   First num will be (i) value, then left pointer and a right pointer
#   Left pointer will be immediate next number, right pointer will be input end
#   Setup up left pointer = i+1, right = rightmost
# Check sum of all 3, move pointers accordingly to conditions which will be
#   Because we have already sorted
#   If too small, increment left
#   If too big, decrease right
#   Repeat until sum = zero OR left = right
#   If triplet is found, append to result
#   Go to next [i]


def solution(input):
    res = set()
    seen_nums = set()
    input.sort()

    for i, val in enumerate(input):
        if val in seen_nums:
            continue
        seen_nums.add(val)
        
        left = i + 1
        right = (len(input)) - 1

        while left < right:
            triplet = val + input[left] + input[right]
            if triplet < 0:
                left += 1
            elif triplet > 0:
                right -= 1
            else:
                res.add((val, input[left], input[right]))
                left += 1

    return res


# ==================================================================================================
# RUN TEST CASES
# ==================================================================================================
if __name__ == "__main__":
    test_cases = [
        # (input, output)
        ([-1,0,1,2,-1,-4], [(-1,-1,2),(-1,0,1)]),
        ([0,1,1], [])
    ]

    for input, output in test_cases:
        print("====== BEGIN CASE:", input)
        if solution(input) != output:
            print("[FAIL]", "EXPECTED:", output)
        else:
            print("[PASS]")