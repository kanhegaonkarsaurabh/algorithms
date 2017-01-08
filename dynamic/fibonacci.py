def fibonacci(n):
    memo, f = [0] * (n + 1), 0
    for i in range(1, n + 1):
        if i <= 2:
            f = 1
        else:
            f = memo[i - 1] + memo[i - 2]
        memo[i] = f
    return memo[n]
