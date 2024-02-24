def solution(x, n):
    return [i * x for i in range(1, n + 1)]


x, n = map(int, input().split())
print(solution(x, n))
