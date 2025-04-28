def non_repeating_character(s):
    # Create a dictionary to store the frequency of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Find the first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char
    
    # If there is no non-repeating character
    return '$'

# Example usage:
s = "geeksforgeeks"
print(non_repeating_character(s))  # Output: 'f'
