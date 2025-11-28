# Python Program to Check Prime Number
# Prime number is a number that is only divisible by 1 and itself. 


def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True
n = int(input("Enter the number: "))

if is_prime(n):
    print(n, "is prime number")
else:
    print(n, "isn't prime number")