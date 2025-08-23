def solution(n):
    answer = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            answer.append(i)
            while n % i == 0:
                n //= i
        else:
            i += 1
    if n > 1:
        answer.append(n)
    return answer