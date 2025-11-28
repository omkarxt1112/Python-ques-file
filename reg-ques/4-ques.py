# Swap Two Variables in Python
# Method 1: Using a Temporary Variable
a = 5
b = 10

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# Method 2: Without Using a Temporary Variable (Tuple Unpacking)
x = 15
y = 20
x, y = y, x
print("After swapping:")
print("x =", x)
print("y =", y)