def count_palindromic_subsequences(test_cases):
    # Initialize an empty list to store results
    results = []
    
    # Iterate over each test case
    for sequence in test_cases:
        # Create a dictionary to store character frequencies
        char_frequency = {}
        
        # Count the frequency of each character
        for char in sequence:
            char_frequency[char] = char_frequency.get(char, 0) + 1
        
        # Initialize a variable to store the count of palindromic subsequences
        palindromic_subsequences = 0
        
        # Calculate the count of palindromic subsequences
        for count in char_frequency.values():
            palindromic_subsequences += count // 2
        
        # Append the result to the list
        results.append(palindromic_subsequences)

    
    
    # Return the list of results
    return results


#Main Program


# Read the number of test cases
num_test_cases = int(input("Number of test cases: "))

# Read the test cases
test_cases = [input("Enter your input here: ").strip() for _ in range(num_test_cases)]

# Call the function to count palindromic subsequences
results = count_palindromic_subsequences(test_cases)

# Print the results
for result in results:
    print(result)

