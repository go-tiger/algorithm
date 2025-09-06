import math

def solution(balls, share):
    answer = 1
    while share:
        answer *= balls / share
        balls -= 1
        share -= 1
    return round(answer)