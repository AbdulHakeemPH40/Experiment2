import math

def calculate_cylinder_volume(radius, height):
    area = math.pi * radius ** 2
    volume = area * height
    return volume

# Get user input
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = calculate_cylinder_volume(radius, height)
print(f"The volume of the cylinder is: {volume}")
