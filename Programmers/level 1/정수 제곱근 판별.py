import math


def solution(n):
    return (math.isqrt(n) + 1) ** 2 if math.isqrt(n) ** 2 == n else -1


n = int(input())
print(solution(n))
