# Fibonacci Sequence: Python Program to display the Fibonacci sequence up to n-th term
# The Fibonacci Sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.
# For example, the Fibonacci sequence up to 7 terms is: 0, 1, 1, 2, 3, 5, 8

# Method 1: (Method 2 is the best method) Using while loop
n_terms = int(input("Enter the number of terms in Fibonacci sequence: "))
n1, n2 = 0, 1
count = 0
if n_terms <= 0:
    print("Please enter a positive integer")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# Method 2: Using function (Best Method)
def fibonacci_sequence(n):
    n1, n2 = 0, 1
    count = 0
    sequence = []
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        sequence.append(n1)
    else:
        while count < n:
            sequence.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    return sequence
num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))
print("Fibonacci sequence:")
print(fibonacci_sequence(num_terms))