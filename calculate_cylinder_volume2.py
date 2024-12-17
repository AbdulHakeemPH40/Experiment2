import math

def calculate_cylinder_volume(radius, height):
    area = math.pi * radius ** 2
    volume = area * height
    return volume

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except:
            print("Invalid input. Please enter a numerical value.")

radius = get_positive_float("Enter the radius of the cylinder: ")
height = get_positive_float("Enter the height of the cylinder: ")


volume = calculate_cylinder_volume(radius, height)
print(f"The volume of the cylinder is: {volume}")
