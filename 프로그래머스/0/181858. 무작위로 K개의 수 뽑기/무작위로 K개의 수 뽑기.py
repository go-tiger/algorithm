def solution(arr, k):
    unique_elements = list(dict.fromkeys(arr))
    answer = unique_elements[:k]
    while len(answer) < k:
        answer.append(-1)
    return answer