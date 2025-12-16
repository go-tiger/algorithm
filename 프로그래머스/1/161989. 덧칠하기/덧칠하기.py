def solution(n, m, sections):
    answer = 0
    painted = 0
    for section in sections:
        if painted < section:
            answer += 1
            painted = section + m - 1
    return answer