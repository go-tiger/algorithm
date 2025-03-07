def solution(array, height):
    answer = 0
    for value in array:
        if value > height:
            answer += 1
    return answer
