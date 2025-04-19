def maximumProfit(prices):
    # Initialize the minimum price seen so far to the first price
    minSoFar = prices[0]
    
    # Initialize maximum profit to 0
    profit = 0

    # Iterate through the list of prices
    for i in range(len(prices)):
        # Update the minimum price if a lower one is found
        minSoFar = min(minSoFar, prices[i])
        
        # Calculate the profit if bought at minSoFar and sold at current price
        # Update maximum profit if this profit is higher
        profit = max(profit, prices[i] - minSoFar)

    # Return the maximum profit found
    return profit
# print(maximumProfit([7,10,4,3,5,7,8,5,12]))