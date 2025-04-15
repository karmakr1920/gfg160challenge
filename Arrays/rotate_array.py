# Function to rotate an array 'arr' to the left by 'd' positions
def rotateArray(arr, d):
    n = len(arr)
    d %= n  # In case d is greater than the length of the array

    # Step 1: Reverse the first 'd' elements
    reverse(arr, 0, d - 1)
    
    # Step 2: Reverse the remaining 'n - d' elements
    reverse(arr, d, n - 1)
    
    # Step 3: Reverse the whole array
    reverse(arr, 0, n - 1)

    return arr  # Return the rotated array

# Helper function to reverse elements in the array from index 'start' to 'end'
def reverse(arr, start, end):
    while start < end:
        # Swap elements at 'start' and 'end'
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage
# print(rotateArray([1, 4234, 534, 3, 6, 4], 2))
