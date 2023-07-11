ropes = int(input())
weight = []
for _ in range(ropes):
    weight.append(int(input()))

result = []
weight.sort(reverse=True)
for i in range(ropes):
    result.append(weight[i] * (i + 1))

print(max(result))