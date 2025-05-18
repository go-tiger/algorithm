def solution(number):
    total_sum = 0
    for digit_char in number:
        total_sum += int(digit_char)
    return total_sum % 9