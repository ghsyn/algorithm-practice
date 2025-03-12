import heapq

def solution(n, works):
    heap = [-i for i in works]
    heapq.heapify(heap)
    
    while n > 0 and heap[0] < 0:
        max_val = heapq.heappop(heap)
        heapq.heappush(heap, max_val + 1)
        n -= 1
        
    answer = sum(i**2 for i in heap)
        
    return answer