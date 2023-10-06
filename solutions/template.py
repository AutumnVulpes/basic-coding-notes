def solution(input):
    # Solution goes here    


# ==================================================================================================
# RUN TEST CASES
# ==================================================================================================
if __name__ == "__main__":
    test_cases = [
        # (input, output)
        ([], False),
    ]

    for input, output in test_cases():
        print("====== BEGIN CASE:", input)
        if solution(input) != output:
            print("[FAIL]", "EXPECTED:", output)
        else:
            print("[PASS]")