def solution(a, d, included):
    answer = 0
    for index, item in enumerate(included):
        if item:
            answer += a + (d * index)
    return answer