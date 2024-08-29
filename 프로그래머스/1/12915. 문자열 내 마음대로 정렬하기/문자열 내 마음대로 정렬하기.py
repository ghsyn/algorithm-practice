def solution(strings, n):
    answer = []
    new_strings = []
    
    for i in strings:
        new_strings.append(i[n] + i)
    new_strings.sort()
    
    for i in new_strings:
        answer.append(i[1:])
    return answer