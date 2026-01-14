import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
_dq = deque(i for i in range(1, n + 1))

while len(_dq) > 1:
    _dq.popleft()
    _dq.rotate(-1)

print(_dq[0])