import math

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def to_base_k(n, k):
    if n == 0:
        return "0"
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        res = chars[n % k] + res
        n //= k
    return res

def solution(n, k):
    answer = 0
    num = to_base_k(n, k)
    num_arr = num.split("0")

    for s_num in num_arr:
        if s_num:
            if is_prime_number(int(s_num)):
                answer += 1
    return answer