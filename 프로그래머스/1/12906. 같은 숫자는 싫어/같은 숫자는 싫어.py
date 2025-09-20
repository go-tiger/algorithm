def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == len(arr) - 1 or arr[i] != arr[i+1]:
            answer.append(arr[i])
    return answer