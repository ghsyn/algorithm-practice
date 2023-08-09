from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())
list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
list.sort()

end = [list[0][1]]

for i in range(1, n):
    heappush(end, list[i][1])
    if end[0] <= list[i][0]:
        heappop(end)

print(len(end))