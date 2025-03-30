def solution(num_list):
    total_sum = 0
    total_mul = 1
    
    for num in num_list:
        total_mul *= num
        total_sum += num
        
    total_sum = total_sum ** 2
    
    if total_mul < total_sum:
        return 1
    return 0