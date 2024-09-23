def solution(sizes):
    answer = 0
    w = h = 0
    
    for card_w, card_h in sizes:
        if card_w < card_h:
            card_w, card_h = card_h, card_w
        w = max(w, card_w)
        h = max(h, card_h)
    
    answer = w * h
    return answer