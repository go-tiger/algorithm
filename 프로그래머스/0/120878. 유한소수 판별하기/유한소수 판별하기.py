def solution(a, b):
    g = 1
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            g = i
    b = b // g
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    return 1 if b == 1 else 2