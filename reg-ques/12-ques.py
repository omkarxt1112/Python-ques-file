# Find the Factorial of a Number
# Factorial numver means multiplying that number by every number before it.
# For example, the factorial of 5 is 5*4*3*2*1 = 120

# Method 1: Using for loop
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

# Method 2: Using function
def factorial_function(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact
number = int(input("Enter a number: "))
print("The factorial of", number, "is", factorial_function(number))