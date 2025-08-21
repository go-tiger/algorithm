def solution(price, money, count):
    total_cost = price * count * (count + 1) // 2
    if total_cost > money:
        return total_cost - money
    else:
        return 0