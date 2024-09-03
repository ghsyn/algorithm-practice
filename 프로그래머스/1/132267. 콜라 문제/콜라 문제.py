def solution(a, b, n):
    answer = 0
    
    while n >= a:
        c, d = divmod(n, a)
        answer += c*b
        n = c*b + d
    
    return answer