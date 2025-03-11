from collections import deque

def bfs(start, target, maps):
    rows, cols = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == target:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] != 'X' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1

def solution(maps):
    start, lever, exit = None, None, None
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                exit = (r, c)
    
    to_lever = bfs(start, lever, maps)
    if to_lever == -1:
        return -1
    
    to_exit = bfs(lever, exit, maps)
    if to_exit == -1:
        return -1

    return to_lever + to_exit
