def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    idx = 0
    
    while(idx + m <= len(score)):
        min = score[idx + m - 1]
        answer += min * m
        # score = score[m:]
        idx += m
            
    return answer