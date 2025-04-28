def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]