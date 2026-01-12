from collections import deque

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    _data = input().strip()[1:-1]
    if n > 0:
        dq = deque(_data.split(","))
    else:
        dq = deque()
    r = 1
    is_error = False
    
    for i in p:
        if i == "R":
            r *= -1
        elif i == "D":
            if len(dq) < 1:
                is_error = True
                break
            if r > 0:
                dq.popleft()
            else:
                dq.pop()
    if is_error:
        print("error")
    else:
        if r < 0:
            dq.reverse()
        print("[" + ",".join(dq) + "]")