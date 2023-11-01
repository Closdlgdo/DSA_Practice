# Write a function that takes a list and removes any duplicate elements.
def remove_duplicates(lst):
    return list(set(lst))


print(remove_duplicates([1, 2, 4, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]))