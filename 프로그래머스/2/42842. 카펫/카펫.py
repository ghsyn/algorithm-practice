def solution(brown, yellow):
    for h in range(1, yellow+1):
        if yellow % h == 0:
            w = yellow // h
            if brown == (h+2) * (w+2) - yellow:
                return [max(w+2, h+2), min(w+2, h+2)]