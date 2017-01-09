def min_change(coins, target):
    change = [0] * (target + 1)
    for i in range(1, target + 1):
        values = [1 + change[i - 1]]
        for c in range(len(coins)):
            if coins[c] <= i:
                values.append(1 + change[i - coins[c]])
        change[i] = min(values)
    return change[target]
