def add (x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply (x,y):
    return x * y

def devide(x,y):
    if y !=0:
        return x/y
    else:
        return "Cannot divide by zero"

def calulator():
    print("Select Operations:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter Choice (1/2/3/4):").strip()

    if choice in ['1','2','3','4',]:
        num1 = float(input("Enter the First Number:"))
        num2 = float(input("Enter the Second Number:"))

        if choice == '1':
            print(f"The result of the Addition is: {add(num1,num2)}")
        elif choice == '2':
            print(f"The result of the Subtraction is :{subtract(num1,num2)}")
        elif choice == '3':
            print(f"The result of the Multiplication is :{multiply(num1,num2)}")
        elif choice == '4':
            print(f"The result of the Division is : {devide(num1,num2)}")
    else:
        print("Invalid Input")

calulator()
