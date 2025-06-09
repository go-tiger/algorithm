def solution(a, b):
    str_ab = str(a) + str(b)
    str_ba = str(b) + str(a)

    num_ab = int(str_ab)
    num_ba = int(str_ba)

    return max(num_ab, num_ba)