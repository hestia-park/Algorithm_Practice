def max_profit(N, M, genetic_info, investment_costs):
    # Initialize the prefix sum of investment costs
    prefix_sum = [0]
    for cost in investment_costs:
        prefix_sum.append(prefix_sum[-1] + cost)

    # Initialize the maximum profit
    max_profit = float('-inf')

    # Iterate over all possible segments of length M or greater
    for i in range(N - M + 1):
        # Calculate the total investment cost for the segment
        total_cost = prefix_sum[i + M] - prefix_sum[i]

        # Calculate the expected profit for the segment
        expected_profit = sum(genetic_info[i:i + M])

        # Calculate the total profit (expected profit - total cost)
        total_profit = expected_profit - total_cost

        # Update the maximum profit
        max_profit = max(max_profit, total_profit)

    return max_profit

# Example input
N = 8
M = 4
genetic_info = [0, 1,1,0,1,1,2,0]
investment_costs = [1,0,0,1,0,0,0,1]

# Calculate the maximum profit
result = max_profit(N, M, genetic_info, investment_costs)
print(f"주어진 유전 정보에 대한 최대 수익은: {result}")
