def solution(arr, queries):
    for s, e, k in queries:
        for j in range(s, e + 1):
            if j % k == 0:
                arr[j] += 1
    return arr