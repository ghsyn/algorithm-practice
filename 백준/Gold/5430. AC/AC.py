from collections import deque

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    _data = input().strip()[1:-1]
    _dq = deque(_data.split(',')) if n > 0 else deque()
    r = 1
    is_error = False
    
    for i in p:
        if i == "R":
            r *= -1
        elif i == "D":
            if len(_dq) < 1:
                is_error = True
                break
                
            if r > 0:
                _dq.popleft()
            else:
                _dq.pop()
        else:
            is_error = True
        
    if is_error:
        print("error")
    else:
        if r < 0:
            _dq.reverse()
        print('[' + ','.join(_dq) + ']')