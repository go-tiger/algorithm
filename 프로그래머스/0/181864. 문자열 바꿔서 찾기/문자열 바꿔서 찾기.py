def solution(myString, pat):
    answer = ""
    for char in myString:
        if char == "A":
            answer += "B"
        else:
            answer += "A"
            
    return 1 if pat in answer else 0