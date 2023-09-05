print("wow")
print("u.u")

# Print index and elements as pairs
for i, j in enumerate(["a", "b", "c"]):
    print(i, j)

for i in enumerate(["a", "b", "c"]):
    print(i)

for i, j in enumerate(["a", "b", "c"]):
    print(i)

for i, j in enumerate(["a", "b", "c"], 2):
    print(i, j)

nums = [0, 1, 2, 3]
print(nums[1:])  # 1, 2, 3
print(nums[:-1])  # 0, 1, 2
print(nums[:-2])  # 0, 1
print(nums[::-1])  # 3, 2, 1, 0
print(nums[2:3])  # 2

print("---")

# Print range starting from 0 and ending before 10
# (10 elements)
for i in range(10):
    print(i)

print("---")

# Print range starting with 1 and ending right before 3
for i in range(1, 3):
    print(i)

print("---")

# Print range starting with 1 and ending right before 10
# But with step size of 2
for i in range(0, 10, 2):
    print(i)

print("---")

# Print each elements
for i in ['a', 'b', 'c']:
    print(i)