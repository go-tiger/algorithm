def solution(arr):
    answer = list(arr)
    min_length = 1

    while min_length < len(arr):
        min_length *= 2

    num_zeros_to_add = min_length - len(arr)
    answer.extend([0] * num_zeros_to_add)
    return answer