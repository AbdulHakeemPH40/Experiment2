# Function to calculate maximum number of palindromic subsequences
def max_palindromic_subsequences(s):
    # Dictionary to store the frequency of each character
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Initialize count of palindromic subsequences
    count = 0
    
    # Calculate pairs for each character
    for char in frequency:
        pairs = frequency[char] // 2  # Number of pairs for this character
        count += pairs  # Add to total count
    
    return count

# Main function to handle multiple test cases
def main():
    # Read number of test cases
    T = int(input("Enter number of test cases: "))
    
    # Process each test case
    for _ in range(T):
        # Read the input string and remove any extra spaces
        s = input("Enter the string: ").strip()
        
        # Calculate and print the result
        result = max_palindromic_subsequences(s)
        print(result)

# Entry point of the program
if __name__ == "__main__":
    main()
