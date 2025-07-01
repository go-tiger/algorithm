def solution(n):
    arr = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                arr[i] += 1
    
    return len([v for v in arr if v >= 3])