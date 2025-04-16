def nextPermutation(arr):
    # Length of the list
    n = len(arr)
    # Store the pivot point (centre)
    centre = -1

    # Step 1: Find the pivot - the first element from the right that is smaller than the one next to it
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            centre = i
            break

    # Step 2: If no pivot exists, reverse the whole list (already the last permutation)
    if centre == -1:
        arr.reverse()
        return arr

    # Step 3: Find the smallest element on the right of the pivot that is larger than arr[centre]
    for i in range(n - 1, centre, -1):
        if arr[i] > arr[centre]:
            arr[i], arr[centre] = arr[centre], arr[i]
            break

    # Step 4: Reverse the suffix (part after the pivot) to get the next permutation
    left, right = centre + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# Test the function
# print(nextPermutation([2, 4, 1, 7, 5, 0]))
