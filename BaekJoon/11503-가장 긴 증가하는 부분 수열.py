n = int(input())
arr = list(map(int,input().split()))


def lis(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)

# 테스트
# arr = [10, 20, 10, 30, 20, 50]
print(lis(arr))