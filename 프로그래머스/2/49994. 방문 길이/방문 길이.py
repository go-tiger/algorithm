def solution(dirs):
    direction = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    visited = set()
    now = [0, 0]

    for dir_char in dirs:
        dx, dy = direction[dir_char]
        nx, ny = now[0] + dx, now[1] + dy

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
            
        visited.add(f"{now[0]}{now[1]}{nx}{ny}")
        visited.add(f"{nx}{ny}{now[0]}{now[1]}")

        now = [nx, ny]
        
    return len(visited) // 2