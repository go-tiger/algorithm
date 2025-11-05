def solution(num, total):
    answer = []
    sum_of_natural_numbers = num * (1 + num) / 2
    start_value = int((total - sum_of_natural_numbers) / num)
    for i in range(num):
        answer.append(start_value + i + 1)
    return answer