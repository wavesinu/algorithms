n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 각 좌표에서 시작하는 최대 크기의 직사각형을 저장할 배열
dp = [[0] * m for _ in range(n)]

# 배열을 순회하면서 각 좌표에서 시작하는 최대 크기의 직사각형을 구함
for i in range(n):
    for j in range(m):
        # 현재 좌표의 값이 양수인 경우
        if arr[i][j] > 0:
            # 좌측 상단 좌표가 배열 범위 내에 있고, 해당 좌표의 값이 양수인 경우
            if i > 0 and j > 0 and arr[i-1][j] > 0 and arr[i][j-1] > 0:
                # 현재 좌표에서 시작하는 최대 크기의 직사각형은, 좌측 상단 좌표에서 시작하는 직사각형의 크기 + 1
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            else:
                # 현재 좌표에서 시작하는 최대 크기의 직사각형은 1
                dp[i][j] = 1

# 최대 크기의 직사각형을 저장할 변수
max_size = 0

# 모든 좌표를 순회하면서 최대 크기의 직사각형을 찾음
for i in range(n):
    for j in range(m):
        max_size = max(max_size, dp[i][j])

# 최대 크기의 직사각형이 없는 경우 -1을 출력, 그렇지 않은 경우 최대 크기를 출력
print(max_size if max_size > 0 else -1)