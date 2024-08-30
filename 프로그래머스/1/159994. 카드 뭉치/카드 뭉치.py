def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1) != 0 and i == cards1[0]:
            cards1.remove(i)
            answer = 'Yes'
        elif len(cards2) != 0 and i == cards2[0]:
            cards2.remove(i)
            answer = 'Yes'
        else:
            return 'No'
    return answer