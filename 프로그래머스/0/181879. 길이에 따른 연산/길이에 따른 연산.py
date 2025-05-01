from functools import reduce

def solution(num_list):
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        answer = reduce(lambda a, b: a * b, num_list, 1)
    return answer