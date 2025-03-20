def solution(n):
    count = sum(1 for i in range(1, n + 1) if n % i == 0)
    return 1 if count % 2 == 1 else 2