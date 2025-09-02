from heapq import heappush, heappop

N, P = map(int, input().split())
A = map(int, input().split())

heap = []
answer = []
fi = -1
sum = 0

for a in A:
    heappush(heap, a)
    sum += a
    while sum - heap[0] >= P:
        sum -= heappop(heap)
    if sum >= P:
        fi = len(heap)
    answer.append(fi)

print(*answer)