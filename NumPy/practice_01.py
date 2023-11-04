# What is NumPy? NumPy is like a special tool for people who work with numbers a lot, especially in programming.
# It makes it much easier to do math and work with big sets of numbers. Imagine if you had to do a lot of calculations
# with a bunch of numbers, like adding, subtracting, or even more complicated stuff. NumPy helps you do all of that
# faster and more efficiently. It's like having a powerful calculator that understands how to handle lots of numbers all
# at once. This can be really handy for tasks like data analysis, scientific computations, and more!
# It is faster to read fewer bytes of memory. Also, there is no type checking when iterating through objects.
# NumPy uses contiguous memory.
# How to access/change specific elements of a numpy array:
import numpy as np

a = np.array(
    [["carlos", 2, 3, 4, 5, 6, "joel"], ["joel", 6, 7, 8, 9, 10, "carlos"], ["Lucas", 62, 57, 28, 39, 130, "Matias"]])
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

# Initializing Different types of Arrays.
# ALL 0s matrices
print(np.zeros((2, 2)))

# ALL 1s matrices
print(np.ones((2, 2)))

# Any number
print(np.full((2, 4), 37))
print(np.full_like(a, 7))

# Initialize an array with random values
print(np.random.randint(-4, 4, size=(3, 3)))

# Identity matrix
print(np.identity(2))

# Repeat an array
array = np.array([[1, 2, 3, 3]])
r1 = np.repeat(array, 3, axis=0)
print(r1)

# Create an array that is a 5x5 matrix where the outside values are 1s, inner is 0s and a single 9 in the middle.
r2 = np.ones((5, 5))
r2[1:-1, 1:-1] = 0
r2[2, 2] = 9
print(r2)
