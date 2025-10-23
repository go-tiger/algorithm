def solution(food):
    answer_parts = []
    for i in range(1, len(food)):
        count = food[i] // 2
        answer_parts.append(str(i) * count)
    first_half = "".join(answer_parts)
    return first_half + '0' + first_half[::-1]