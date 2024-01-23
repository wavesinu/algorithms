import sys


def promising(i, col):
    for k in range(1, i):
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            return False
    return True


def nqueens(i, col):
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            global count
            count += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                nqueens(i + 1, col)


n = int(sys.stdin.readline())
col = [0] * (n + 1)
count = 0
nqueens(0, col)

print(count)
