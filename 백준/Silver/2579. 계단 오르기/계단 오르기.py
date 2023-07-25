n = int(input())
list = [int(input()) for _ in range(n)]
dp = []

if (len(list) <= 2):
    print(sum(list))
else:
    dp.append(list[0])
    dp.append(list[0] + list[1])
    dp.append(max(list[0] + list[2], list[1] + list[2]))
    for i in range(3, n):
        dp.append(max(dp[i - 3] + list[i] + list[i - 1], dp[i - 2] + list[i]))
    print(dp[n - 1])