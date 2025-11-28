# How to Calculate Area of Triangle

def area_of_triangle(base, height):
    return 0.5 * base * height
# Example usage
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = area_of_triangle(base, height)
print(f"The area of the triangle with base {base} and height {height} is {area}")
