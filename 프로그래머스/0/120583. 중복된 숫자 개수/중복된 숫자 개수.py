def solution(array, n):
    answer = 0
    for item in array:
        if n == item:
            answer += 1
    return answer
