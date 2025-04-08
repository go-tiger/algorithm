def solution(numbers):
    numbers.sort()
    a = numbers[-1] * numbers[-2]
    b = numbers[0] * numbers[1]
    return max(a, b)