def solution(n, lost, reserve):
    reserve.sort()
    lost.sort()
    
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    
    for i in reserve[:]:
        if i-1 in lost:
            lost.remove(i-1)
            reserve.remove(i)
        elif i+1 in lost:
            lost.remove(i+1)
            reserve.remove(i)
            
    answer = n - len(lost)
    return answer