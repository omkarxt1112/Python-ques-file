# Python Program to Check Leap Year
# A year is a leap year if:
# 1. It is divisible by 4.
# 2. Except century years (divisible by 100).
# 3. Unless also divisible by 400.

# Method 1: Using the standard leap year rules (Most Common)
year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Method 2: Using a Function
def is_leap(year):
      return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

year = int(input("Enter the Year: "))

if is_leap(year):
      print(year, "is a leap year")
else:
      print(year, "is not a leap year")