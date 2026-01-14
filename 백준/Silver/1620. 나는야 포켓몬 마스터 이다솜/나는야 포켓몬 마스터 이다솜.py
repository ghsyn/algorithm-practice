import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(1, n + 1):
    name = input().strip()
    dict[str(i)] = name
    dict[name] = str(i)

for _ in range(m):
    _quiz = input().strip()
    print(dict[_quiz])