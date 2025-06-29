def solution(x):
    num_str = str(x)

    digit_sum = 0
    for digit_char in num_str:
        digit_sum += int(digit_char)
    return x % digit_sum == 0