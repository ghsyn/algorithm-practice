T = int(input())

results = []

for _ in range(T):
    stack = []
    s = input()
    isVPS = True
    
    for ch in s:
        if ch == '(':
            stack.append('(')
        if ch == ')':
            if stack:
                stack.pop()
            elif not stack:
                isVPS = False
                break
    
    if not stack and isVPS:
        results.append('YES')
    elif stack or not isVPS:
        results.append('NO')
        
for result in results:
    print(result)