def solution(order):
    answer = 0
    for od in order:
        if "americano" in od:
            answer += 4500
        elif "cafelatte" in od:
            answer += 5000
        elif "anything" in od:
            answer += 4500
    return answer