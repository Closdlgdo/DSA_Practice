# What is NumPy? NumPy is like a special tool for people who work with numbers a lot, especially in programming.
# It makes it much easier to do math and work with big sets of numbers. Imagine if you had to do a lot of calculations
# with a bunch of numbers, like adding, subtracting, or even more complicated stuff. NumPy helps you do all of that
# faster and more efficiently. It's like having a powerful calculator that understands how to handle lots of numbers all
# at once. This can be really handy for tasks like data analysis, scientific computations, and more!
# It is faster to read fewer bytes of memory. Also, there is no type checking when iterating through objects.
# NumPy uses contiguous memory.
# How to access/change specific elements of a numpy array:
import numpy as np

a = np.array([["carlos", 2, 3, 4, 5, 6, "joel"], ["joel", 6, 7, 8, 9, 10, "carlos"], ["Lucas", 62, 57, 28, 39, 130, "Matias"]])
print(a)

# Get a specific element [row, col]
print(a[1, 0])

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:, 2])

# Get fancy [startindex:endindex:stepsize]
print(a[0, 1:-1:2])

# Change a specific element
a[1, 0] = "Theano"
print(a)

# Change a specific row
a[1, :] = "Theano"
print(a)

# Change a specific column
a[:, 2] = "New Column"
print(a)

# Get specific element
var = a[0, 2]
print(var)