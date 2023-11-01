# Create a list comprehension that generates a list of squares of even numbers from 1 to 10.

squares = [x**2 for x in range(1, 11) if x % 2 == 0]  # This is a list comprehension

print(squares)


# for x in range(1, 11): This part of the list comprehension sets up a loop. It iterates through numbers from 1 to 10.
# if x % 2 == 0: This is a conditional statement. It checks if the current value of x is even (x % 2 == 0). If it is, the condition is
# True, and the value is included in the list.
# **x**: This is the expression that gets evaluated and added to the list. In this case, it's x itself.
# x** squared (x2`)**: This is the expression that calculates the square of x.