def solution(n):
    digits = list(str(n))
    digits.sort(reverse=True)
    sorted_str = ''.join(digits)
    return int(sorted_str)