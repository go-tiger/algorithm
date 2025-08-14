import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        sqrt_i = math.sqrt(i)
        if sqrt_i.is_integer():
            answer -= i
        else:
            answer += i
    return answer