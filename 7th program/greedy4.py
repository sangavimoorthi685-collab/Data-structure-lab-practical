n = int(input("Enter number of items: "))

value = list(map(int, input("Enter values: ").split()))
weight = list(map(int, input("Enter weights: ").split()))

capacity = int(input("Enter capacity: "))

dp = [0] * (capacity + 1)

for i in range(n):
    for w in range(capacity, weight[i] - 1, -1):
        dp[w] = max(dp[w], value[i] + dp[w - weight[i]])

print("Maximum Profit:", dp[capacity])