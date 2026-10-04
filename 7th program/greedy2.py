n = int(input("Enter number of items: "))

values = []
weights = []

for i in range(n):
    v, w = map(int, input("Enter value and weight: ").split())
    values.append(v)
    weights.append(w)

capacity = int(input("Enter capacity: "))

dp = [[0] * (capacity + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Profit:", dp[n][capacity])