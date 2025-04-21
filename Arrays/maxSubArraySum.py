# Function to find the maximum sum of a contiguous subarray using Kadane's Algorithm
def maxSubArraySum(arr):
    # Initialize result and maxEnding with the first element of the array
    res = arr[0]
    maxEnding = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update maxEnding to be the maximum of the current element or current element + previous maxEnding
        maxEnding = max(maxEnding + arr[i], arr[i])
        # Update the result if maxEnding is greater than the current result
        res = max(res, maxEnding)
    
    # Return the maximum subarray sum found
    return res

# Example usage: prints the maximum subarray sum from the given list
# print(maxSubArraySum([2, 3, 5, -3, 8, 2]))
