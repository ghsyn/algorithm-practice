from collections import deque

def solution(n, edge):
    answer = 0
    edge.sort()
    
    graph = [[] for i in range(n + 1)]    
    for i in range(len(edge)):
        a, b = edge[i]
        graph[a].append(b)
        graph[b].append(a)
    
    route = [0] * (n + 1)
    q = deque()
    q.append(1)
    route[1] = 1
    
    while q:
        now = q.popleft()
        for g in graph[now]:
            if route[g] == 0:
                q.append(g)
                route[g] = route[now] + 1
        
    return route.count(max(route))