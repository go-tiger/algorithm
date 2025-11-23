def solution(number, limit, power):
    res = 0

    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if i // j == j:
                    cnt += 1
                else:
                    cnt += 2
            if cnt > limit:
                cnt = power
                break
        res += cnt
    return res