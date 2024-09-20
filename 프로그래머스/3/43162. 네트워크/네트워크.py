def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(pc):
        if pc < 0 or pc >= n:
            return answer
        
        visited[pc] = True
        
        for con_pc, is_connect in enumerate(computers[pc]):
            if is_connect == 1 and visited[con_pc] == False:
                dfs(con_pc)
    
    for computer in range(n):
        if visited[computer] == False:
            dfs(computer)
            answer += 1
    
    return answer