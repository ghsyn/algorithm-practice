import sys

input = sys.stdin.readline

k = int(input().strip())
_stack = list()

for _ in range(k):
    num = int(input().strip())
    _stack.pop() if num == 0 else _stack.append(num)

print(sum(_stack))