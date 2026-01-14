k = int(input())
_stack = []

for _ in range(k):
    num = int(input())
    _stack.append(num) if num != 0 else _stack.pop()
    
print(sum(_stack))