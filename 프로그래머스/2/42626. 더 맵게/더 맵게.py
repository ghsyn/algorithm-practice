import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        
        if len(scoville) < 2:
            return -1
        
        first_val = heapq.heappop(scoville)
        second_val = heapq.heappop(scoville)
        heapq.heappush(scoville, first_val + second_val * 2)
        answer += 1
    
    return answer