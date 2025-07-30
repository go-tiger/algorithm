def solution(arr):
    min_value = min(arr)
    if len(arr) == 1:
        return [-1]
    return [x for x in arr if x != min_value]