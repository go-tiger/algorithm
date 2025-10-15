def solution(a, b, n):
    answer = 0
    while n >= a:
        received_bottles = (n // a) * b
        answer += received_bottles
        n = received_bottles + (n % a)
    return answer