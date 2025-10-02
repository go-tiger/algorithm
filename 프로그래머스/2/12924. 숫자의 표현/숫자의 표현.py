def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 1:
            answer += 1   
    return answer