def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        current_min = float('inf') 
        for j in range(s, e + 1):
            if arr[j] > k and arr[j] < current_min:
                current_min = arr[j]
        if current_min == float('inf'):
            answer.append(-1)
        else:
            answer.append(current_min)
    return answer