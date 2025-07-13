def solution(arr, queries):
    answer = list(arr)
    for query in queries:
        idx1, idx2 = query
        answer[idx1], answer[idx2] = answer[idx2], answer[idx1]
    return answer