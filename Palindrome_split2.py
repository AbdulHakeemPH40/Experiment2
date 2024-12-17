def is_palindrome(s):
    """
    This function checks if a given string 's' is a palindrome.
    A palindrome reads the same forward and backward.
    """
    return s == s[::-1]

def max_palindromic_subsequences(s):
    """
    This function calculates the maximum number of non-overlapping palindromic subsequences
    that can be created from the given string 's'. Each palindromic subsequence must have
    a length greater than 1.
    """
    n = len(s)  # Get the length of the string
    used = [False] * n  # Create a list to track used characters
    palindromes = []  # List to store palindromic subsequences

    # Find all palindromic subsequences
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                l, r = i, j
                # Check if the substring between s[i] and s[j] is a palindrome
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:  # Found a palindrome
                    palindromes.append((i, j))  # Append the indices of the palindrome

    # Sort palindromes by length in descending order
    palindromes.sort(key=lambda x: x[1] - x[0], reverse=True)

    count = 0  # Initialize the count of non-overlapping palindromic subsequences
    for p in palindromes:
        # Check if the current palindrome overlaps with previously used characters
        if not any(used[p[0]:p[1] + 1]):
            # Mark characters of the current palindrome as used
            for k in range(p[0], p[1] + 1):
                used[k] = True
            count += 1  # Increment the count for each valid palindrome

    return count

# Main block to read input and print results
if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))  # Read number of test cases
    for _ in range(t):
        s = input("Enter the string: ").strip()  # Read the string
        print(max_palindromic_subsequences(s))  # Print the result for each test case
