from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    visited = [[0] * cols for _ in range(rows)]
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    q = deque()
    
    q.append((0, 0))
    visited[0][0] = 1
    
    if rows >= 2 and cols >= 2:
        if maps[rows - 1][cols - 2] == 0 and maps[rows - 2][cols - 1] == 0:
            pass
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < rows and 0 <= nx < cols:
                if maps[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

    result = visited[rows - 1][cols - 1]
    
    if result == 0:
        return -1
    else:
        return result