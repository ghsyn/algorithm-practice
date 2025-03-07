from collections import deque

def solution(n, wires):
    graph = {i : [] for i in range(1, n+1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    answer = float('inf')
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        size = dfs(a, graph)
        answer = min(answer, abs((n - size) - size))
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer

def dfs(node, graph):
    visited = set()
    need_visited = deque([node])
    
    while need_visited:
        node = need_visited.pop()
        
        if node not in visited:
            visited.add(node)
            need_visited.extend(graph[node])
            
    return len(visited)