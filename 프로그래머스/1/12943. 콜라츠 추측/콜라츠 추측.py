def solution(num):
    for i in range(500):
        if num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 + 1
        else:
            return i
    return -1