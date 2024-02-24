def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])


def solution_v2(n):
    # num / 2의 수들만 검사하면 성능 향상
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])