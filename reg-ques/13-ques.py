# Display the Multiplication Table of a Given Number

# Method 1: Using for loop
num = int(input("Enter a number to display its multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Method 2: Alternative Method: Using a function
def multiplication_table(n):
    print(f"Multiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
number = int(input("Enter a number to display its multiplication table: "))
multiplication_table(number)