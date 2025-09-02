T = int(input())
answer = []

while T > 0:
    T -= 1
    L, R, S = list(map(int, input().split()))
    
    for x in range(1, R - L + 1):
        if x % 2 == 0:
            S += x - 1
        elif x % 2 == 1:
            S -= x - 1

        if S == L or S == R:
            answer.append(x)
            break

for i in answer:
    print(i, end='\n')