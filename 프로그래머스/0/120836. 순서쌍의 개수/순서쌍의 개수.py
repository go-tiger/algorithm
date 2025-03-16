def solution(n):
    answer = sum(1 for i in range(1, n + 1) if n % i == 0)
    return answer