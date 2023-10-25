# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Solution:
# We can use hashmap to store the value and its frequency.
nums = [1, 2, 2, 3, 3, 4]


def containsDuplicate(my_nums):
    hashset = set()

    for n in my_nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


# **hashset = set():**
# *This line creates an empty collection called hashset that can hold unique items. It's like having an empty box to put things in.*
#
# **for n in nums::**
# *This starts a loop that goes through each number (n) in a list of numbers called nums. It's like looking at each item in a shopping list, one by one.*
#
# **if n in hashset::**
# *This line checks if the current number n is already in the hashset. It's like checking if you've already seen this item in your shopping list before.*
#
# **return True:**
# *If the number is already in the hashset, it means there's a duplicate, so the function immediately stops and says "Yes, there's a duplicate!" It's like saying "Yes, I've already seen this item in my list!"*
#
# **hashset.add(n):**
# *If the number is not in the hashset, it means it's a new item. So, we add it to our collection. It's like adding a new item to our box.*
#
# **return False:**
# *If the loop finishes without finding any duplicates, it means all the items are unique. So, the function says "No, there are no duplicates." It's like saying "All items in my list are different."*