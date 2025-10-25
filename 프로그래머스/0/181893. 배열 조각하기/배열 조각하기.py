def solution(arr, query):
    answer = list(arr)
    for i, q_val in enumerate(query):
        if i % 2 == 0:
            answer = answer[:q_val + 1]
        else:
            answer = answer[q_val:]
    return answer