def factorial(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

try:
    N = int(input("Enter a number to calculate its factorial: ")).strip()
    print(f"The factorial of {N} is {factorial(N)}")
except:
    print("Invalid input. Please enter an integer value.")
