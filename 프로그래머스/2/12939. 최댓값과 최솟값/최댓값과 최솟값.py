def solution(s):
    arr = list(map(int, s.split(' ')))
    return f"{min(arr)} {max(arr)}"