import sys
input = sys.stdin.readline

k = int(input())
_stack = []

for _ in range(k):
    x = int(input())
    _stack.pop() if x == 0 else _stack.append(x)
    
print(sum(_stack))