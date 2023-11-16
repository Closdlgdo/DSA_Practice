# Write a Python function that takes a list of numbers as input and returns the maximum element in the list.

# def max_element(nums):
#     max_num = nums[0]
#     for num in nums:
#         if num > max_num:
#             max_num = num
#     return max_num
#
#
# print(max_element([1, 3, 43, 554, 65]))

# Line 3: # This line defines a Python function named max_element that takes one argument, nums.
#     # This function is designed to find the maximum element in a list of numbers.
# Line 4: # This line initializes a variable max_num to the first element of the list nums. This is where
#     # we start our search for the maximum element.
# Line 5: # This line starts a loop that iterates through each element in the list nums. The loop variable
#     # num will take on the value of each element in nums one by one.
# Line 6: if num > max_num:: This line starts an if statement. It checks if the current element num
#     # is greater than the current maximum max_num.
# Line 7: # If the condition num > max_num is true, this line updates max_num to be the value of num,
#     # making it the new maximum.
# Line 8: # This line is outside the loop and if statement. It means that once the loop has finished iterating through all
#     # elements, the function will return the maximum element found, which is stored in max_num.
nums = [1, 3, 43, 554, 65]
max_element = ([num for num in nums if num == max(nums)])
print(max_element)