from collections import defaultdict

def find_max_nodes(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)

    max_count = 0
    max_nodes = []
    for node in range(1, n+1):
        visited = [False] * (n+1)
        count = dfs(node, graph, visited)
        if count > max_count:
            max_count = count
            max_nodes = [node]
        elif count == max_count:
            max_nodes.append(node)

    return max_nodes

def dfs(node, graph, visited):
    if visited[node]:
        return 0
    visited[node] = True
    count = 1
    for neighbor in graph[node]:
        count += dfs(neighbor, graph, visited)
    return count

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = find_max_nodes(n, edges)
print(*result)