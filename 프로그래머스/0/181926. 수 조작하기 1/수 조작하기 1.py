def solution(n, control):
    answer = n
    for char in control:
        if char == 'w':
            answer += 1
        elif char == 's':
            answer -= 1
        elif char == 'd':
            answer += 10
        elif char == 'a':
            answer -= 10
    return answer