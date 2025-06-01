def solution(num, k):
    num_str = str(num)
    k_str = str(k)

    index = num_str.find(k_str)

    if index != -1:
        return index + 1
    else:
        return -1