n = int(input())
list = list(map(int, input().split()))
res = 0

honeys = []
honeys.append(list[0])
for i in range(1, n):
    honeys.append(honeys[i - 1] + list[i])

for i in range(1, n - 1):
    res = max(res, 2 * honeys[-1] - list[0] - list[i] - honeys[i])
       
for i in range(1, n - 1):
    res = max(res, honeys[-1] - list[-1] - list[i] + honeys[i - 1])
    
for i in range(1, n - 1):
    res = max(res, honeys[-1] - list[0] - list[-1] + list[i])

print(res)