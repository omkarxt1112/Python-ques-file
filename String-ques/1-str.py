# Check Whether a String is Palindrome or Not in Python
# A palindrome is a word, phrase, number, or other sequences of characters which reads the same backward as forward, such as madam or racecar.
# in simple terms, it is a string that remains unchanged when reversed.
# For example, "madam" is a palindrome because it reads the same backward.
# examples: wow, level, radar, civic, rotor. these are all palindromes.

# Method 1: Using function using string slicing
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

