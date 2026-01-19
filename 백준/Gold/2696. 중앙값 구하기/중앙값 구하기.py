import sys, heapq

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    m = int(input().strip())
    print(m // 2 + 1)
    
    _list = []
    while len(_list) < m:
        _list.extend(map(int, input().split()))
    
    min_heap = []
    max_heap = []
    results = []
    
    for idx, val in enumerate(_list):
        if not max_heap or val <= -max_heap[0]:
            heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(min_heap, val)
            
        if (idx + 1) % 2 == 1:
            size = len(max_heap) - len(min_heap)
            if size > 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif size < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            results.append(str(-max_heap[0]))
        
    for i in range(0, len(results), 10):
        print(' '.join(results[i:i+10]))