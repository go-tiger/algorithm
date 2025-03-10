def solution(n):
    answer = 0
    n_str = str(n)
    for digit in n_str:
        answer += int(digit)
    return answer
