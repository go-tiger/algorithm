def solution(arr, n):
    if len(arr) % 2 == 1:
        return [num + n if i % 2 == 0 else num for i, num in enumerate(arr)]
    else:
        return [num + n if i % 2 == 1 else num for i, num in enumerate(arr)]