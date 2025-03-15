def solution(slice, n):
    answer = 0
    while n > slice * answer:
        answer += 1
    return answer