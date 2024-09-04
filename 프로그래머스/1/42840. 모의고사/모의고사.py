def solution(answers):
    pick = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    student = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if pick[0][i%5] == answers[i]:
            student[1] += 1
        if pick[1][i%8] == answers[i]:
            student[2] += 1
        if pick[2][i%10] == answers[i]:
            student[3] += 1
    
    answer = [k for k, v in student.items() if v == max(student.values())]
    return answer