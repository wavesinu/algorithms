def count_ways(n, memo=None):
    if memo is None:
        memo = [-1] * (n + 1)

    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = count_ways(n-2, memo) + count_ways(n-3, memo)
    return memo[n] % 10007

n = int(input())

result = count_ways(n)
if result > 0:
    print(result)
else:
    print(0)