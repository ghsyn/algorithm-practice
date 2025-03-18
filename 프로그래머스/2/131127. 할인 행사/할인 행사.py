from collections import Counter

def solution(want, number, discount):
    best_day = 0
    want_number = dict(zip(want, number))
    
    for i in range(len(discount) - 10 + 1):
        if want_number == Counter(discount[i:i + 10]):
            best_day += 1
            
    return best_day