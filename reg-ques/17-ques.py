# Find the Sum of Natural Numbers using the Python Program
# Natural numbers are the set of positive integers starting from 1.
# For example, the sum of first 5 natural numbers is 1 + 2 + 3 + 4 + 5 = 15

# Method 1: Using for loop
num = int(input("Enter a positive integer: "))
if num < 1:
    print("Please enter a positive integer.")
else:
    sum_natural = sum(range(1, num + 1))
    print(f"The sum of the first {num} natural numbers is: {sum_natural}")
    
# Method 2: Using function
def sum_of_natural_numbers(n):
    if n < 1:
        return "Please enter a positive integer."
    else:
        return sum(range(1, n + 1))
number = int(input("Enter a positive integer: "))
print(f"The sum of the first {number} natural numbers is: {sum_of_natural_numbers(number)}")
