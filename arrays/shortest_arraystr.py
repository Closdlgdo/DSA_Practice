# We will try to sort some an array of strings then
# try and print out the shortest string.

def shortest_string(arr):
    arr.sort(key=len)
    return arr[0]


print(shortest_string(["Agglutination", "Absorbefacient", "Batrachophagous", "Flibbertigibbet", "Juglandaceous"]))

# Here's a breakdown of what happens:

# arr.sort(key=len): This sorts the list arr based on the length of its elements. The shortest string will come first after this operation.
# return arr[0]: This returns the first element of the sorted list, which is the shortest string.

