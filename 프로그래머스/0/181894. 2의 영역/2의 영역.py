def solution(arr):
    try:
        start_index = arr.index(2)
        end_index = len(arr) - 1 - arr[::-1].index(2)
        return arr[start_index : end_index + 1]
    except ValueError:
        return [-1]