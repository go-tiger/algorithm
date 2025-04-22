def solution(arr):
    answer = []
    for s in arr:
        for _ in range(s):
            answer.append(s)
    return answer