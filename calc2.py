def add (a,b):
    return a + b

def subrtract (a,b):
    return a - b

def multiply (a,b):
    return a * b

def devide (a,b):
    if b != 0:
        return a/b
    else:
        return ("Cannot Divide by Zero")
    
def calcuator():
    print("Selection:")
    print('1.Add:')
    print('2:Subtract')
    print('3.Multiply')
    print('4.Divide')

    choice = input("Enter a choice (1/2/3/4):").strip()

    if choice in ['1','2','3','4']:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        if choice == '1':
            print(f"The result of Addition is:{add(num1,num2)}")
        elif choice == '2':
            print(f"The result of Subtraction is:{subrtract(num1,num2)}")
        elif choice == '3':
            print(f"The result of the multiplication is: {multiply(num1,num2)}")
        elif choice == '4':
            print(f"The result of the devide is: {devide(num1,num2)}")
    else:
        print("Invalid Input")


calcuator()
