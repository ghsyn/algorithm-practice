n = int(input())
cards = list(map(int, input().split()))
dict = {}
answer = -1

for i in range(2 * n):
    if cards[i] in dict:
        answer = max(answer, i - dict[cards[i]] - 1)
    else:
        dict[cards[i]] = i

print(answer)