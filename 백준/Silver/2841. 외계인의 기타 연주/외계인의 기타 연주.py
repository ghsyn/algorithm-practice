import sys

input = sys.stdin.readline

n, p = map(int, input().split())
stack = [[] for _ in range(7)]
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    while stack[x] and stack[x][-1] > y:
        stack[x].pop()
        cnt += 1

    if not stack[x] or stack[x][-1] < y:
        stack[x].append(y)
        cnt += 1

print(cnt)