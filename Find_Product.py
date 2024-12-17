# Define the modulo constant
MOD = 10**9 + 7

# Prompt user for the number of elements
# try:
N = int(input("Enter the number of elements in the array (N): "))
# except ValueError:
#     print("Error: N must be an integer.")
#     exit()

# Prompt user for the elements of the array
# try:
A = list(map(int, input(f"Enter {N} integers separated by spaces: ").split()))
#     if len(A) != N:
#         print(f"Error: Expected {N} integers, but got {len(A)}.")
#         exit()
# except ValueError:
#     print("Error: Please enter valid integers separated by spaces.")
#     exit()

# Initialize the product
product = 1

# Calculate the product of all numbers modulo MOD
for num in A:
    product = (product * num) % MOD

# Print the result
print("The product modulo", MOD, "is:", product)
