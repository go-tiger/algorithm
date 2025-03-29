def solution(a, b):
    ab = str(a) + str(b)
    ab2 = 2 * a * b
    
    answer = max(int(ab), ab2)
    return answer