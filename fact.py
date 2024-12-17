import sys
sys.set_int_max_str_digits(10**5)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input("Enter a Number:"))
print(factorial(n))
