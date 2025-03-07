def solution(n, wires):
    graph = {i : [] for i in range(1, n+1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    answer = float('inf')
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        visited = set()
        
        def dfs(node, graph):
            visited.add(node)

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    dfs(i, graph)

            return len(visited)
        
        size = dfs(a, graph)
        answer = min(answer, abs((n - size) - size))
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer