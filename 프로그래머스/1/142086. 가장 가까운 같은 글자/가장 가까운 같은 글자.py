def solution(s):
    answer = [-1] * len(s)
    for i in range(len(s) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if s[i] == s[j]:
                answer[i] = i - j
                break
    return answer