def solution(t, p):
    sub = []
    answer = 0
    
    for i in range(len(t)):
        if i > len(t) - len(p):
            break
        sub.append(t[i:i+len(p)])
    
    for i in sub:
        if int(i) <= int(p):
            answer += 1
    return answer