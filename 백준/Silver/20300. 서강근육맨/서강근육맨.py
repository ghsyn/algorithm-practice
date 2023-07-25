n = int(input())
t = list(map(int, input().split()))
t.sort()

if (n % 2 == 0):
    m = 0
    for i in range(n // 2):
        if (m < t[i] + t[n - 1 - i]):
            m = t[i] + t[n - 1 - i]
else:
    m = t[n - 1]
    for i in range(n // 2):
        if (m < t[i] + t[n - 2 - i]):
            m = t[i] + t[n - 2 - i]

print(m)
