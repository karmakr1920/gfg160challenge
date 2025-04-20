def getMinDiff(arr, k):
    # Step 1: Get the length of the array
    n = len(arr)

    # Step 2: Sort the array to simplify finding min/max and making decisions
    arr.sort()

    # Step 3: Initialize the result as the current max difference (without any changes)
    res = arr[n - 1] - arr[0]

    # Step 4: Loop through the array to try different partition points
    # We start from i = 1 because we need at least one element on each side of the partition
    for i in range(1, n):

        # Step 5: If decreasing this value by k results in negative height, skip this partition
        if arr[i] - k < 0:
            continue

        # Step 6: Calculate the minimum height possible after modification
        # Either increase the smallest element or decrease the current element
        minH = min(arr[0] + k, arr[i] - k)

        # Step 7: Calculate the maximum height possible after modification
        # Either increase the element just before i, or decrease the last element
        maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        # Step 8: Update the result if the current max-min difference is smaller
        res = min(res, maxH - minH)

    # Step 9: Return the minimum difference found
    return res

# print(getMinDiff([3,5,32,2,6,34],3))
