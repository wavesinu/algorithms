from collections import deque


def bfs(n, m, h, board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                start_x, start_y = i, j
                break

    queue = deque([(start_x, start_y, m)])
    board[start_x][start_y] = -1
    count = 0

    while queue:
        x, y, health = queue.popleft()
        if board[x][y] == 2:
            health += h
            count += 1
            board[x][y] = -1  # 방문 지점을 표시

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != -1:
                if health - 1 >= 0:  # 체력이 0 이상이면 이동
                    queue.append((nx, ny, health - 1))
                    board[nx][ny] = -1  # 방문 표시

    return count


n, m, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs(n, m, h, board))
