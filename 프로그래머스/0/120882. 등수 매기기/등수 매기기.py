def solution(score):
    answer = [1] * len(score)
    avg = [(s[0] + s[1]) / 2 for s in score]
    
    for i in range(len(avg)):
        for j in range(len(avg)):
            if avg[i] < avg[j]:
                answer[i] += 1
    return answer