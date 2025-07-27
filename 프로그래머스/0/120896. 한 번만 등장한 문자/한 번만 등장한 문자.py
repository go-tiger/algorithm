def solution(s):
    answer = []
    for char in s:
        if s.find(char) == s.rfind(char):
            answer.append(char)
    answer.sort()
    return "".join(answer)