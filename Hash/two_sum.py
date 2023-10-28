# We are given an array of integers nums and an integer target.
# Return true if any two integers in nums add up to target.
# Return false if none of the integers in nums can add up to target.

# Example: nums = [4, 7, 11, 15], target = 18

# Given list of numbers
nums = [3, 2, 4, 5, 9, 1]

# The target sum we want to achieve
target = 10

# Initialize a dictionary to store visited numbers
visited_nums = {}

# Iterate through each number in the list
for num in nums:
    # Calculate the number needed to reach the target
    needed_num = target - num

    # Check if the needed number is in the visited numbers dictionary
    if needed_num in visited_nums:
        # If it is, it means we've found a pair that adds up to the target
        print(f"{needed_num} + {num} = {target}")
        break

    # If not, add the current number to the visited numbers dictionary
    visited_nums[num] = True
