def solution(n, computers):
    networks = 0
    visit = [False] * n

    def dfs(index):
        visit[index] = True
        
        computer_row = computers[index]
        
        for i in range(n):
            if computer_row[i] == 1 and not visit[i]:
                dfs(i)

    for i in range(n):
        if not visit[i]:
            networks += 1
            dfs(i)
    return networks