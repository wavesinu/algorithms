def count_climb(n):
    if n == 0:
        return 1 % 10007  # 0층에서는 올라갈 필요가 없으므로 방법의 수는 1
    dp = [0] * (n + 1)
    dp[0] = 1  # 초기 상태 설정
    for i in range(1, n + 1):
        if i >= 2:
            dp[i] += dp[i - 2] % 10007  # 2계단 전에서 오는 방법의 수
        if i >= 3:
            dp[i] += dp[i - 3] % 10007  # 3계단 전에서 오는 방법의 수
        dp[i] %= 10007  # 매 단계마다 모듈러 연산 적용
    return dp[n]

# 입력 받기
n = int(input())

# 결과 계산 및 출력
result = count_climb(n)
print(result if result != 0 else 0)