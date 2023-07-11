citys = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = roads[0] * costs[0]
min_costs = costs[0]

for i in range(1, citys - 1):
    if min_costs > costs[i]:
        min_costs = costs[i]
    result += min_costs * roads[i]

print(result)