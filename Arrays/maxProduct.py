def maxProduct(arr):
    n = len(arr)

    # Initialize current minimum and maximum products to the first element
    currMin = arr[0]
    currMax = arr[0]

    # Initialize the result (maximum product found so far)
    maxprod = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Store the max product temporarily, considering:
        # 1. Current number alone
        # 2. Product with previous min (could become max if arr[i] is negative)
        # 3. Product with previous max
        temp = max(arr[i], currMin * arr[i], currMax * arr[i])

        # Update current min product (for possible future use)
        currMin = min(arr[i], currMin * arr[i], currMax * arr[i])

        # Update current max product
        currMax = temp

        # Update overall max product result
        maxprod = max(currMax, maxprod)

    return maxprod
