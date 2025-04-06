def solution(my_string):
    answer = []
    for char in my_string:
        if ord(char) < 58:
            answer.append(int(char))
    return sorted(answer)