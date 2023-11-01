# Write a function that reverses a given string.
def reverse_string(input_string):
    return input_string[::-1]


print(reverse_string("Delgado").title())

# Line 3: return input_string[::-1]
# This line uses string slicing to reverse the input string. The [::-1] part creates a new string that is a reversed
# version of input_string.
# This is a string slicing notation in Python. It allows you to extract a portion of a string.
# The first : indicates the start of the slice.
# The second : before 1 indicates the end of the slice.
# The -1 after the second : indicates the step size. In this case, -1 means that you're iterating over the string in reverse.
# So, [::-1] means "start from the beginning, end at the end, and move in steps of -1" which effectively reverses the string.