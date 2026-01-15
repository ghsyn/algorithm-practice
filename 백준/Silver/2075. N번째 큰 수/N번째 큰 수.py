import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    _readline = map(int, input().split())
    
    if not heap:
        heap = list(_readline)
    else:
        for i in _readline:
            if heap[0] < i:
                heapq.heapreplace(heap, i)
                
print(heap[0])