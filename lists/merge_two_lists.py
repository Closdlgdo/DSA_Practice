# Write a function that takes two lists and returns a new list containing all the elements from both lists and then removes
# duplicates.

def merge_lists(list1, list2):
    joined_list = list1 + list2
    return list(set(joined_list))


print(merge_lists([1, 2, 3, 6], [3, 4, 5, 6]))