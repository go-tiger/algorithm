def solution(board):
    answer = 0
    mine_deltas = [
        (-1, 0), (1, 0), (0, 1), (0, -1),
        (-1, 1), (1, 1), (1, -1), (-1, -1)
    ]
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                for dr, dc in mine_deltas:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == 0:
                            board[nr][nc] = 2               
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 0:
                answer += 1    
    return answer