def solution(lottos, win_nums):
    answer = []
    win_cnt = 0
    
    for i in lottos:
        if i in win_nums:
            win_cnt += 1
    
    max = 7 - (win_cnt + lottos.count(0))
    min = 7 - win_cnt
    
    answer.append(6 if max == 7 else max)
    answer.append(6 if min == 7 else min)
               
    return answer