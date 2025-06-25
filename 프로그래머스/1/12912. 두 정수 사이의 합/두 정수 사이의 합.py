def solution(a, b):
    answer = 0
    add = min(a, b)
    for _ in range(abs(b - a) + 1):
        answer += add
        add += 1
    return answer