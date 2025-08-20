def solution(bin1, bin2):
    int_bin1 = int(bin1, 2)
    int_bin2 = int(bin2, 2)
    sum_int = int_bin1 + int_bin2
    return bin(sum_int)[2:]