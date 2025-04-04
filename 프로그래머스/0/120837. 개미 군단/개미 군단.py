def solution(hp):
    antG = hp // 5
    antS = (hp - antG * 5) // 3
    antI = hp - antG * 5 - antS * 3

    return antG + antS + antI