def solution(n):
    original_one_count = bin(n).count('1')
    
    while True:
        n += 1
        if bin(n).count('1') == original_one_count:
            return n