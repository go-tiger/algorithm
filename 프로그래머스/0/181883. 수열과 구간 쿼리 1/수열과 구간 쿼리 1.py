def solution(arr, queries):
    answer = list(arr)
    for query in queries:
        s, e = query
        for j in range(s, e + 1):
            answer[j] += 1
    return answer