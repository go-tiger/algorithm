import math

def solution(s):
    length = len(s)
    
    if length % 2 != 0:
        return s[length // 2]
    else:
        mid_right_idx = length // 2
        mid_left_idx = mid_right_idx - 1
        return s[mid_left_idx] + s[mid_right_idx]