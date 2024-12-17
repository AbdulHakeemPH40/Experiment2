S = input("Enter Your Input Here:")  # Takes input from the user

reverse_S = S[::-1]  # Reverses the string

if S == reverse_S:  # Checks if the original and reversed strings are the same
    print("YES")
else:
    print("NO")
