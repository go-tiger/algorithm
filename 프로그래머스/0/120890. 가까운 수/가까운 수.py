import math

def solution(array, n):
    array.sort()

    differ = float('inf') 
    answer = 0
    
    for i in array:
        current_diff = abs(n - i)
        if current_diff < differ:
            differ = current_diff
            answer = i
        elif current_diff == differ and i < answer:
            answer = i
    return answer