text = input("Enter text: ")

# Remove all spaces...
text = text.replace(' ','')

# ... and check if the word is equal to reversed itself
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("It's a palindrome")
else:
	print("It's not a palindrome")


# Lab 2.5.7 - Palindromes
#
# Purpose:
# Check whether the text entered by the user is a palindrome.
#
# Assumptions:
# 1. The user enters a string of text.
# 2. An empty string is not a palindrome.
# 3. Uppercase and lowercase letters are treated equally.
# 4. Spaces are ignored when checking for a palindrome.
# 5. The text must read the same forward and backward.
#
# Tracing:
# 1. Ask the user to enter text.
# 2. Remove all spaces from the text.
# 3. Check that the text contains more than one character.
# 4. Convert the text to uppercase for comparison.
# 5. Reverse the text using [::-1].
# 6. Compare the original text with the reversed text.
# 7. Print whether the text is a palindrome.