# Write a function that counts the number of words in a sentence.
def count_words(sentence):
    return len(sentence.split())


print(count_words("How many words are in this sentence?"))

# Line 3: return len(sentence.split())
# This line contains the logic to count the words. Here's what it does:
# sentence.split() splits the input sentence into a list of words. By default, it splits on spaces, so it separates the
# words.
# len(...) gets the length of the list of words, which is effectively the number of words in the sentence.
# So, len(sentence.split()) gives you the count of words.