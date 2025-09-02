T = int(input())
answer = []

while T > 0:
    T -= 1
    L, R, S = list(map(int, input().split()))

    x = 2 * (S - L) if S < ((L + R) / 2) else 2 * (R - S) - 1
    answer.append(x + 1)

for i in answer:
    print(i, end='\n')