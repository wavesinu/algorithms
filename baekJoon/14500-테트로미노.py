def max_tetromino_sum(board, N, M):
    visited = [[False] * M for _ in range(N)]
    max_sum = 0

    # 테트로미노를 구성하는 4개의 칸을 탐색하는 DFS 함수
    def dfs(x, y, depth, current_sum):
        nonlocal max_sum
        if depth == 4:  # 4개의 칸을 모두 탐색했다면
            max_sum = max(max_sum, current_sum)
            return
        # 상하좌우 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, current_sum + board[nx][ny])
                visited[nx][ny] = False

    # 모든 칸을 시작점으로 하여 DFS 실행
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, board[i][j])  # 시작점도 카운트에 포함
            visited[i][j] = False

    return max_sum

# 입력 받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_tetromino_sum(board, N, M))