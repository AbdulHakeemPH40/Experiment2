def factorial(_):
    result = 1
    for i in range(1, _ +1):
        result *=i
    return result

N = 5  # Test value, replace it with any number you want to test
print(factorial(N))
