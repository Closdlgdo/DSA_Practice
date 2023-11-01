# Given an array, rotate the array to the right by a given number of steps.
def rotate_array(arr, steps):
    return arr[-steps:] + arr[:-steps]


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # output: [5, 6, 7, 1, 2, 3, 4]

# Line 3: This line of code is using list slicing and concatenation to perform a right rotation on the input array arr
# by a specified number of steps (steps). Let's break it down step by step:
# arr[-steps:]:
# This is list slicing. It selects a portion of the list arr starting from the index -steps to the end of the list.
# Negative indices count from the end of the list. So, arr[-steps:] selects the last steps elements of the list.
# arr[:-steps]:
# This is also list slicing. It selects a portion of the list arr from the beginning to the index -steps. So, arr[:-steps]
# selects all elements except the last steps elements.
# return arr[-steps:] + arr[:-steps]:
# Here, we're concatenating the two slices obtained in the previous steps. This effectively places the last steps
# elements at the beginning of the list, resulting in a right rotation.
# For example, if arr = [1, 2, 3, 4, 5] and steps = 2, arr[-steps:] would be [4, 5] (the last 2 elements) and arr[:-steps]
# would be [1, 2, 3] (all elements except the last 2). When concatenated, you get [4, 5, 1, 2, 3], which is the array
# rotated to the right by 2 steps.

# There is also this approach:


def rotate_array(arr, step):
    step = step % len(arr)  # Handle cases where step is greater than the length of the array.
    return arr[-step:] + arr[:-step]


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 5))  # output: [3, 4, 5, 6, 7, 1, 2]

# This approach first calculates k % len(arr) to handle cases where k is greater than the length of the array.
# Then, it slices the array into two parts: the last k elements (arr[-k:]) and the remaining elements (arr[:-k]).
# Finally, it concatenates these two parts.