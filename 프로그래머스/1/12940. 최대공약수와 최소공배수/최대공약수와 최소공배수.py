def solution(n, m):
    a = min(n, m)
    b = max(n, m)
    
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return [i, (a * b) // i]
    return []