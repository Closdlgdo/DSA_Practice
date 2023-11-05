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

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")

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

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")

# MATH OPERATIONS

# Addition
a = np.array([4, 3, 2])
b = np.array([4, 5, 6])
result = np.add(a, b)
print(result)

# Add to each number in the array
a = np.array([1, 5, 6])
print(a + 2)

# Subtraction
a = np.array([4, 2, 4])
b = np.array([4, 5, 6])
result = np.subtract(a, b)
print(result)

# Subtract to each number in the array
a = np.array([1, 5, 6])
print(a - 2)

# Multiplication
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.multiply(a, b)
print(result)

# Multiply to each number in the array
a = np.array([1, 5, 6])
print(a * 7)

# Division
a = np.array([13, 250, 30])
b = np.array([4, 8, 6])
result = np.divide(a, b)
print(result)

# Divide to each number in the array
a = np.array([100, 50, 37])
print(a / 2)

# Exponentiation
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
result = np.power(a, b)
print(result)

# Exponent to each number in the array
a = np.array([4, 3, 7])
print(a ** 5)

# Square root
a = np.array([4, 9, 16])
result = np.sqrt(a)
print(result)

# Square to each number in the array
a = np.array([1, 5, 6])
print(a ** 2)

# Trigonometric functions
a = np.array([0, np.pi/2, np.pi])
result = np.sin(a)
print(result)
result = np.cos(a)
print(result)
result = np.tan(a)
print(result)

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")

# LINEAR ALGEBRA

a = np.ones((2, 3))
print(a)
b = np.full((3, 2), 2)
print(b)

print(np.matmul(a, b))

# Determinant of a matrix
c = np.identity(3)
print(np.linalg.det(c))

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")

# STATISTICS OPERATIONS: SUM, MEAN, STD, VARIANCE, MIN, MAX, CORRELATION, COVARIANCE, MODE.
stats = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(stats)
# find Min
print(np.min(stats))
# find Max
print(np.max(stats))
# find Mean
print(np.mean(stats))
# find Standard Deviation
print(np.std(stats))
# find Variance
print(np.var(stats))
# find Correlation
# Calculate the correlation of the array 'stats'
correlation = np.corrcoef(stats)
print(correlation)
# Calculate the covariance of the array 'stats'
covariance = np.cov(stats)
print(covariance)
# # Calculate the mode of the array 'stats'
# mode = np.mode(stats)
# print(mode)

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")

# Reorganizing Arrays
before = np.array([[1, 2, 3, 5], [4, 5, 6, 7]])
print(before)
# We are able to change the shape of the array.
after = before.reshape((2, 2, 2))
print(after)

# Vertically Stacking vectors
v1 = np.array([11, 2, 23, 44])
v2 = np.array([54, 25, 16, 7])

print(np.vstack([v1, v2, v1, v2]))

# Horizontally Stacking vectors
v1 = np.array([21, 12, 2, 44])
v2 = np.array([42, 12, 6, 7])

result = np.hstack([v1, v2, v1, v2])
print(result)

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")