n = int(input())
result_list = [input() for i in range(n)]
score_list = [0 for _ in range(n)]
i = 0

while i < n:
    result = result_list[i]
    count = 0

    for isCorrect in result:
        count += 1

        if isCorrect != 'O':
            count = 0

        score_list[i] += count

    i += 1

for i in score_list:
    print(i)