def solution(arr):
    answer = []
    for item in arr:
        if answer and answer[-1] == item:
            answer.pop()
        else:
            answer.append(item)
    return [-1] if not answer else answer