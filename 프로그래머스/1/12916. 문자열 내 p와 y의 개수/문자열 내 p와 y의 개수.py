def solution(s):
    s_upper = s.upper()
    return len(s_upper.split('P')) == len(s_upper.split('Y'))