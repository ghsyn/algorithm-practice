from collections import deque

def solution(maps):
    (n, m) = (len(maps), len(maps[0]))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()
        
            for idx in range(4):
                nx = i + dx[idx]
                ny = j + dy[idx]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[i][j] + 1
                    queue.append((nx, ny))
                
        return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]
    return bfs(0, 0)