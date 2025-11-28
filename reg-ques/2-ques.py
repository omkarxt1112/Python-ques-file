# Q. Find & Calculate Square Root Program in Python
import math
def calculate_square_root(number):
    if number < 0:
        return "Cannot calculate square root of a negative number."
    else:
        return math.sqrt(number)
# Example usage
num = int(input("Enter the number to find sqrt:"))
result = calculate_square_root(num)
print(f"The square root of {num} is {result}")