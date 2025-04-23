def circularSubarraySum(arr):
    # Edge case: empty array
    if not arr:
        return 0

    # Initialize values
    total_sum = arr[0]          # Total sum of the array
    current_max = arr[0]        # Max subarray ending at current position
    current_min = arr[0]        # Min subarray ending at current position
    max_sum = arr[0]            # Global max subarray sum
    min_sum = arr[0]            # Global min subarray sum

    # Loop through the array starting from index 1
    for i in range(1, len(arr)):
        num = arr[i]

        # Standard Kadane's logic to find max subarray sum (non-circular)
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)

        # Kadane's logic for min subarray sum (to handle circular case)
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)

        # Update total sum of the array
        total_sum += num

    # Handle the edge case where all numbers are negative
    if min_sum == total_sum:
        return max_sum

    # The answer is the maximum of:
    # 1. Non-circular max subarray sum
    # 2. Circular max subarray sum = total_sum - min_sum
    return max(max_sum, total_sum - min_sum)

# Example usage:
# arr = [8 ,-8, 9 ,-9, 10, -11, 12]
# print("Maximum circular subarray sum:", circularSubarraySum(arr))
