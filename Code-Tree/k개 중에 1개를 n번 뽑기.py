k, n = map(int, input().split())


def ordered_pair(k, n, result=[]):
    if n == 0:
        print(" ".join(map(str, result)))
        return
    for i in range(1, k + 1):
        ordered_pair(k, n - 1, result + [i])
        
ordered_pair(k, n)


