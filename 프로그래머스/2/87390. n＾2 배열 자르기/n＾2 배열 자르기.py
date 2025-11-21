def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        s = i // n
        r = i % n
        answer.append(max(s, r) + 1)
    return answer