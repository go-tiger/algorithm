def solution(order):
    answer = 0
    order_str = str(order)

    for digit in order_str:
        if digit in ['3', '6', '9']:
            answer += 1
    return answer