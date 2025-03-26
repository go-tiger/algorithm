def solution(array):
    max_value, max_index = max((value, index) for index, value in enumerate(array))
    return [max_value, max_index]