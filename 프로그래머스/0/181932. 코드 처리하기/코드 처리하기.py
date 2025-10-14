def solution(code):
    answer = []
    mode = 0

    for i, char in enumerate(code):
        if char == '1':
            mode = 1 - mode
        else:
            if mode == 0 and i % 2 == 0:
                answer.append(char)
            elif mode == 1 and i % 2 == 1:
                answer.append(char)

    if answer:
        return "".join(answer)
    else:
        return "EMPTY"