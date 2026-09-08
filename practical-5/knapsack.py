# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            weight = weights[i - 1]
            value = values[i - 1]

            # Don't include the current item
            dp[i][w] = dp[i - 1][w]

            # Include the current item if it fits
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    return dp[n][capacity]


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter knapsack capacity: "))

# Calculate maximum value
maximum_value = knapsack(weights, values, capacity)

# ---------------- OUTPUT ----------------

print("\n----- Knapsack Result -----")
print("Maximum value:", maximum_value)
print("Time Complexity: O(n * W)")
print("Space Complexity: O(n * W)")
