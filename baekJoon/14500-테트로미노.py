def max_tetromino_sum(board, N, M):
    # 테트로미노 모양 정의
    tetrominoes = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # I 모양
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # O 모양
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # T 모양
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # S 모양
        [(0, 1), (1, 1), (1, 0), (2, 0)],  # Z 모양
        [(0, 0), (1, 0), (2, 0), (2, 1)],  # J 모양
        [(0, 1), (1, 1), (2, 1), (2, 0)]   # L 모양
    ]

    def get_sum(x, y, shape):
        result = 0
        for dx, dy in shape:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                result += board[nx][ny]
            else:
                return 0
        return result

    max_sum = 0
    for i in range(N):
        for j in range(M):
            for tetromino in tetrominoes:
                # 각 테트로미노에 대해 회전 및 대칭을 고려
                for _ in range(4):  # 회전
                    max_sum = max(max_sum, get_sum(i, j, tetromino))
                    tetromino = [(y, -x) for x, y in tetromino]  # 회전
                for _ in range(2):  # 대칭
                    max_sum = max(max_sum, get_sum(i, j, tetromino))
                    tetromino = [(-x, y) for x, y in tetromino]  # 대칭

    return max_sum

# 입력 받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_tetromino_sum(board, N, M))