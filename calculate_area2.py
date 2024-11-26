def calculate_area(length,width):
    area = length * width
    return area

length = float(input("Enter the length of of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))

result = calculate_area(length,width)

print(f"The area of the recatangle is: {result}")
