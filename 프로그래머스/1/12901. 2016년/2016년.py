def solution(a, b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = 0
    
    for i in range(a-1):
        date += month[i]
    date += b
    
    answer = day[(date+4) % 7]
        
    return answer