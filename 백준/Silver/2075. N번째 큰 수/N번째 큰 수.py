import heapq

n = []

for _ in range(int(input())):
    array = list(map(int, input().split()))
    if not n:
        for i in array:
            heapq.heappush(n, i)
    else:
        for i in array:
            if n[0] < i:
                heapq.heappush(n, i)
                heapq.heappop(n)

print(n[0])