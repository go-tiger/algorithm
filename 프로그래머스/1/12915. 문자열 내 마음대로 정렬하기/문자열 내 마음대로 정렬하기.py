def solution(strings, n):
    strings.sort(key=lambda s: (s[n], s))
    return strings