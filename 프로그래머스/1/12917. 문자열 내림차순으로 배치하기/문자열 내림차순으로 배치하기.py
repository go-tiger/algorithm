def solution(s):
    sorted_chars = sorted(list(s), reverse=True)
    return "".join(sorted_chars)