def solution(str1, str2):
    answer_chars = []
    for char1, char2 in zip(str1, str2):
        answer_chars.append(char1)
        answer_chars.append(char2)
    return ''.join(answer_chars)