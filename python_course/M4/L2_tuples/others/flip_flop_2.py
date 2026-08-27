"""
Activity: Check Whether a Tuple is a Palindrome

Instructions:
1. Create a tuple of numbers.
2. Create a function to check whether the tuple reads the same
   from left to right and right to left.
3. Use a while loop to compare the first and last elements.
4. Return False if any two elements are different.
5. Return True if all elements match.
6. Use an if-else statement to display the result.
"""

numbers = (1, 2, 3, 3, 2, 1)

# Create a function to check whether the tuple is a palindrome
def is_palindrome(numbers):
    start = 0
    end = len(numbers) - 1

    # Compare elements from both ends of the tuple
    while start < end:
        if numbers[start] != numbers[end]:
            return False

        start += 1
        end -= 1

    return True


# Check the result and display the message
if is_palindrome(numbers):
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")