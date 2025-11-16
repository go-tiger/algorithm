import math

def solution(n, a, b):
    ans = 0
    while a != b:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        ans += 1
    return ans