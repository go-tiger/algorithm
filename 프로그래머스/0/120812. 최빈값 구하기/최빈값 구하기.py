def solution(array):
    if not array:
        return -1 
    max_possible_val = max(array) + 1 if array else 1
    res = [0] * max_possible_val
    for num in array:
        res[num] += 1
    max_freq = 0
    if res:
        max_freq = max(res)
    answer = -1
    count_modes = 0
    for i in range(len(res)):
        if res[i] == max_freq:
            answer = i
            count_modes += 1
        if count_modes >= 2:
            return -1 
    return answer