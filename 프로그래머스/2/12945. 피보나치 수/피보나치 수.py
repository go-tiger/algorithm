def solution(n):
    answer = 0
    f0 = 0
    f1 = 1
    for i in range(2, n + 1):
        answer = (f0 + f1) % 1234567
        f0 = f1
        f1 = answer
    return answer