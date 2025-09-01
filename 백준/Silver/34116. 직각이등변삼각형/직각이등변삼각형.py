import sys
input = sys.stdin.readline

N = int(input().strip())
byY = {}
for _ in range(N):
    x, y = map(int, input().split())
    if y not in byY:
        byY[y] = [x, x]
    else:
        if x < byY[y][0]: byY[y][0] = x
        if x > byY[y][1]: byY[y][1] = x

ys = sorted(byY.keys())

def sweep_bottom_up():
    y0 = ys[0]
    L, R = byY[y0]
    L = int(L); R = int(R)

    for y in ys[1:]:
        h = y - y0
        lx, rx = byY[y]
        if lx < L + h:
            L = lx - h
        if rx > R - h:
            R = rx + h
    return R - L

def sweep_top_down():
    y0 = ys[-1]
    L, R = byY[y0]
    L = int(L); R = int(R)

    for y in reversed(ys[:-1]):
        h = y0 - y
        lx, rx = byY[y]
        if lx < L + h:
            L = lx - h
        if rx > R - h:
            R = rx + h
    return R - L

answer = min(sweep_bottom_up(), sweep_top_down())
print(answer)