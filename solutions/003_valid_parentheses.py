# https://leetcode.com/problems/valid-parentheses/

# 0) Create empty stack and dictionary of bracket pairs
# 1) If unit is left bracket, append said unit to stack
# 2) If unit is a right bracket
# 2a) If unit is matching topmost unit on stack: Pop out topmost unit
# of stack
# 2b) Else: Return False
# 3) When string is done, check if stack is empty
# 3a) if stack is  empty, return true

# Creation of input, empty stack and bracket pair keys

def solution(input):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for unit in input:
        if unit in brackets.keys():
            stack.append(unit)
        elif len(stack) == 0:
            return False
        elif unit == brackets[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


# ==================================================================================================
# RUN TEST CASES
# ==================================================================================================
if __name__ == "__main__":
    test_cases = {
        "()":           True,
        "()[]{}":       True,
        "}":            False,
        "{([][](){})}": True,
        "{([][]){}]}":  False,
        "(]":           False,
    }

    for input, output in test_cases.items():
        print("====== BEGIN CASE:", input)
        if solution(input) != output:
            print("[FAIL]", "EXPECTED:", output)
        else:
            print("[PASS]")