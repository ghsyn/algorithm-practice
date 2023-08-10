n = int(input())
k = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

dis = []
for i in range(n - 1):
    dis.append(n_list[i + 1] - n_list[i])

dis.sort(reverse=True)
dis = dis[:k - 1]

res = n_list[-1] - n_list[0]

for i in dis:
    res -= i

print(res)