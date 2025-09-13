def solution(s):
    answer = 0
    for char in s:
        if char == "(":
            answer += 1
        else: # char == ")"
            answer -= 1
        if answer < 0:
            break
    return answer == 0