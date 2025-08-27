def solution(numbers, k):
    answer = 1
    for _ in range(k - 1):
        answer += 2
        if answer > len(numbers):
            answer -= len(numbers)
    return answer