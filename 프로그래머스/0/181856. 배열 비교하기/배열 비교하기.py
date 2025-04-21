def solution(arr1, arr2):
    arr1_sum = sum(arr1)
    arr2_sum = sum(arr2)

    if len(arr1) == len(arr2):
        if arr1_sum > arr2_sum:
            return 1
        elif arr2_sum > arr1_sum:
            return -1
        else:
            return 0

    return 1 if len(arr1) > len(arr2) else -1