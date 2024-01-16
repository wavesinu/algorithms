from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 정점 수, 간선 수, 시작 정점
N, M, V = map(int, input().split())

# 그래프 정보
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 수행
visited = [False] * (N + 1)
dfs(graph, V, visited)
print()

# 방문 정보 초기화
visited = [False] * (N + 1)

# BFS 수행
bfs(graph, V, visited)
print()
