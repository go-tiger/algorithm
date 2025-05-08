def solution(arr, intervals):
    (a, b), (c, d) = intervals
    return arr[a:b+1] + arr[c:d+1]