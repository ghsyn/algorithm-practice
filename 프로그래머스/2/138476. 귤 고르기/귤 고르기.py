from collections import Counter

def solution(k, tangerine):
    answer = 1
    cnt = Counter(tangerine)
    cnt = cnt.most_common()
    
    for key, val in cnt:
        if k - val > 0:
            k -= val
            answer += 1
        else:
            break
        
    return answer