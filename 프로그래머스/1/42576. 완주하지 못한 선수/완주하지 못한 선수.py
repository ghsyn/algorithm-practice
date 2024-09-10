def solution(participant, completion):
    dict = {}
    tmp = 0
    
    for i in participant:
        dict[hash(i)] = i
        tmp += int(hash(i))
        
    for i in completion:
        tmp -= hash(i)
    
    return dict[tmp]