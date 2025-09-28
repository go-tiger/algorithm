def solution(s):
    answer = [0, 0]
    while len(s) > 1:
        answer[0] += 1
        num_zeros = s.count('0')
        answer[1] += num_zeros
        
        num_ones = len(s) - num_zeros
        s = bin(num_ones)[2:] 
    return answer