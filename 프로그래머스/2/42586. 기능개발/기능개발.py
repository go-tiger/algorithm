import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
        
    prev = 0
    
    for i in range(len(days)):
        if days[prev] < days[i]:
            answer.append(i - prev)
            prev = i

    answer.append(len(days) - prev)
    return answer