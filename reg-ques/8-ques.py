# Find the Largest Among Three Numbers
# Method 1:
num1 = int(input("Enter 1st numb: "))
num2 = int(input("Enter 2nd numb: "))
num3 = int(input("Enter 3rd numb: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is highest number.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is highest number.")
else:
    print(f"{num3} is highest number.")

# Method2: Using Function
def largest_numb(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is highest number.")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is highest number.")
    else:
        print(f"{num3} is highest number.")

total = largest_numb(10,1000, 20)