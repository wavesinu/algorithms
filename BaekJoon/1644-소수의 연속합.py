import sys


def is_prime(n):
    li = [False, False] + [True] * (n - 1)
    p = []

    for i in range(2, n+1):
        if li[i]:
            p.append(i)
            for j in range(i * i, n + 1, i):
                li[j] = False

    return p


n = int(sys.stdin.readline())

cnt = 0
start = 0
end = 0

p = is_prime(n)
while start <= end:
    if end == len(p):
        break
    if sum(p[start:end+1]) == n:
        cnt += 1
        end += 1
    elif sum(p[start:end+1]) < n:
        end += 1
    else:
        start += 1

print(cnt)