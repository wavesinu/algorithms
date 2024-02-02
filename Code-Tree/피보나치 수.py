n = int(input())

def fibbo(n, memo=None):
    if memo is None:
        memo = [-1] * (n + 1)

    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fibbo(n - 1, memo) + fibbo(n - 2, memo)
    return memo[n]

print(fibbo(n))