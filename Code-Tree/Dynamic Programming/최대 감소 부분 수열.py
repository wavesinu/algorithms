import sys


INT_MIN = -sys.maxsize

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * (n)

def dp_initializer():
    for i in range(1, n):
        dp[i] = 1
    
    dp[0] = 1
    
dp_initializer()

for i in range(1, n):
    for j in range(0, i):
        if arr[i] < arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))