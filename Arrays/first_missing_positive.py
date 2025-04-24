def first_missing_positive(nums):
    n = len(nums)

    # Place each number in its correct position if possible
    for i in range(n):
        while (
            1 <= nums[i] <= n and
            nums[nums[i] - 1] != nums[i]
        ):
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    # After reordering, the first place where index + 1 != value is the missing number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all positions are correct, the missing number is n + 1
    return n + 1

# Example usage
arr = [3, 4, -1, 1]
print(first_missing_positive(arr))  # Output: 2
