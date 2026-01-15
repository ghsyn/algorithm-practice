import sys
from collections import deque

input = sys.stdin.readline

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
            if len(_dq) == 0:
                is_error = True
                break
            else:
                _dq.popleft() if r > 0 else _dq.pop()
        else:
            is_error = True
    
    if is_error:
        print('error')
    else:
        if r < 1:
            _dq.reverse()
        print('[' + ','.join(_dq) + ']')