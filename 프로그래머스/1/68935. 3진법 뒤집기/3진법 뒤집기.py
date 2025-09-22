def solution(n):
    if n == 0:
        ternary_str = "0"
    else:
        temp_n = n
        digits = []
        while temp_n > 0:
            digits.append(str(temp_n % 3))
            temp_n //= 3
        ternary_str = "".join(reversed(digits))
    reversed_ternary_str = ternary_str[::-1]
    answer = int(reversed_ternary_str, 3)
    return answer