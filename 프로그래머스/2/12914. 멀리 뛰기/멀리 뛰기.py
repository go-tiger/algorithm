def solution(n):
    fi = [0] * (n + 1)
    if n >= 0:
        fi[0] = 1
    if n >= 1:
        fi[1] = 1
    for i in range(2, n + 1):
        fi[i] = (fi[i - 1] + fi[i - 2]) % 1234567
    return fi[n]