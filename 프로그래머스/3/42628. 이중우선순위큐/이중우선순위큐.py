import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    def pop_min():
        node = heapq.heappop(min_heap)
        max_heap.remove(-node)
        heapq.heapify(max_heap)
    def pop_max():
        node = heapq.heappop(max_heap)
        min_heap.remove(-node)
        heapq.heapify(min_heap)
    
    for command in operations:
        com, val = command.split()
        val = int(val)
        
        if com == 'I':
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
        if com == 'D' and min_heap:
                pop_min() if val < 0 else pop_max()
    
    return [max(min_heap), min(min_heap)] if min_heap else [0, 0]