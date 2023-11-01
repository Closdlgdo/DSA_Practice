# Write a function that checks if a given word or phrase is a palindrome.
def palindrome(word, phrase):
    if word == word[::-1] and phrase == phrase[::-1]:
        return "Both word and phrase are a palindrome"
    if word == word[::-1]:
        return "Only the word is a palindrome"
    if phrase == phrase[::-1]:
        return "Only the phrase is a palindrome"
    else:
        return "Not a palindrome"


print(palindrome("racecar", "carlos"))

# Line 3: This is a conditional statement that checks if both the word and phrase are palindromes. It uses string
# slicing to reverse both word and phrase and compares them with their original forms.
# If both are palindromes, it returns the message "Both word and phrase are a palindrome".
# Line 5: if word == word[::-1]:
# This conditional statement checks if only the word is a palindrome. If so, it returns the message
# "Only the word is a palindrome".
# Line 7: if phrase == phrase[::-1]:
# This conditional statement checks if only the phrase is a palindrome. If so, it returns the message
# "Only the phrase is a palindrome".