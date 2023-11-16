# Write a function that reverses an array in-place.
def reverse_array(nums):
    for i in range(len(nums) // 2):
        nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]
    return nums


print(reverse_array([1, 2, 3, 4, 5]))

# Line 3: This line starts a loop that iterates through the first half of the list nums. The loop variable i will take
# on the values from 0 to len(nums) // 2 - 1.
# Line 4: Inside the loop, this line swaps the elements at positions i and len(nums) - i - 1. This effectively reverses
# the order of the elements.
# Suppose i is 0. This means we're swapping the first element (nums[0]) with the last element (nums[len(nums) - 1 - 0]
# which is the same as nums[len(nums) - 1]).
# The assignment looks like this: nums[0], nums[len(nums) - 1] = nums[len(nums) - 1], nums[0]
# After this line, the value at index 0 will be swapped with the value at the last index. This effectively reverses the
# order of the first and last elements.
# This process continues for each iteration of the loop, effectively reversing the entire list.

################################################################

# This is the list comprehension version of the above code.

nums = [1, 2, 3, 4]
print([nums[len(nums) - i - 1] for i in range(len(nums))])
