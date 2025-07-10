def solution(num_list):
    answer = 0
    for num_item in num_list:
        num = num_item
        while num != 1:
            if num % 2 != 0:
                num -= 1
            else:
                num = num // 2
                answer += 1
    return answer