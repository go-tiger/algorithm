def solution(t, p):
    answer = 0
    p_len = len(p)
    p_int = int(p)
    for i in range(len(t) - p_len + 1):
        sub_str = t[i : i + p_len]
        if int(sub_str) <= p_int:
            answer += 1
    return answer