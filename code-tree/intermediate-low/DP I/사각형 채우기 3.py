MOD = 1000000007  # 모듈러 연산을 위한 값 (필요한 경우)


def count_tilings(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 2
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % MOD
        for j in range(i - 3, -1, -1):
            dp[i] = (dp[i] + dp[j] * 2) % MOD
    return dp[n]


n = int(input())
print(count_tilings(n))  # 출력: 7
