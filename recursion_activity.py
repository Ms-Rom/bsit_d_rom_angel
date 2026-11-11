
# Hands-On Activity: Recursive Array Toolkit

# 1. Sum the Array
def sum_array(arr):
    # Base case: An empty array has a sum of 0
    if len(arr) == 0:
        return 0

    # Recursive case: First number + sum of remaining numbers
    return arr[0] + sum_array(arr[1:])


# 2. Find the Largest Number
def find_largest(arr):
    # Input rule: The array must not be empty
    if len(arr) == 0:
        raise ValueError("Array must contain at least one number")

    # Base case: One number is automatically the largest
    if len(arr) == 1:
        return arr[0]

    # Recursive case: Compare first number with the rest
    largest_rest = find_largest(arr[1:])

    if arr[0] > largest_rest:
        return arr[0]
    else:
        return largest_rest


# 3. Count a Chosen Number
def count_number(arr, target):
    # Base case: No numbers left to examine
    if len(arr) == 0:
        return 0

    # Recursive case: Count the first number if it matches
    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)


# TESTING THE FUNCTIONS

print("1. SUM THE ARRAY")
print("Empty array:", sum_array([]))
print("One number:", sum_array([5]))
print("Several numbers:", sum_array([2, 4, -3, 6]))

print("\n2. FIND THE LARGEST NUMBER")
print("One number:", find_largest([8]))
print("Largest at beginning:", find_largest([10, 4, 2, 7]))
print("Largest at end:", find_largest([3, 5, 8, 12]))
print("Negative numbers:", find_largest([-8, -2, -10, -4]))

print("\n3. COUNT A CHOSEN NUMBER")
print("Empty array:", count_number([], 5))
print("Target appears several times:", count_number([2, 5, 3, 5, 5, 8], 5))
print("Target does not appear:", count_number([1, 2, 3, 4], 7))
