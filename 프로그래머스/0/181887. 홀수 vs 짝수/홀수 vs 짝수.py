def solution(num_list):
    sum_even = 0
    sum_odd = 0
    for i, num in enumerate(num_list):
        if i % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return max(sum_even, sum_odd)