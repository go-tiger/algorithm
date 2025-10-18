def solution(cards1, cards2, goal):
    for s in goal:
        if cards1 and cards1[0] == s:
            cards1.pop(0)
        elif cards2 and cards2[0] == s:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"