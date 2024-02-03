def divide(n, nums):
    total = sum(nums)

    if total % 2 != 0:
        return "No"

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return "Yes" if dp[target] else "No"


n = int(input())
nums = list(map(int, input().split()))
print(divide(n, nums))