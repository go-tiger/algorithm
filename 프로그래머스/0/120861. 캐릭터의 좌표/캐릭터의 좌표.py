def solution(keyinput, board):
    answer = [0, 0]
    end_x = (board[0] - 1) // 2
    end_y = (board[1] - 1) // 2
    
    for command in keyinput:
        if command == 'left':
            if answer[0] > -end_x:
                answer[0] -= 1
        elif command == 'right':
            if answer[0] < end_x:
                answer[0] += 1
        elif command == 'up':
            if answer[1] < end_y:
                answer[1] += 1
        elif command == 'down':
            if answer[1] > -end_y:
                answer[1] -= 1        
    return answer