def solution(participant, completion):
    dict = {}
    for i in participant:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
            
    for i in completion:
        if i in dict:
            dict[i] -= 1

    return ''.join([k for k, v in dict.items() if v != 0])