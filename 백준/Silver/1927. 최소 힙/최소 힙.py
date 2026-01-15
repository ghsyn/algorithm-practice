import sys, heapq
input = sys.stdin.readline

n = int(input())
_list = []

for _ in range(n):
    x = int(input())
    
    if x == 0:
        print('0') if not _list else print(heapq.heappop(_list))
    else:
        heapq.heappush(_list, x)