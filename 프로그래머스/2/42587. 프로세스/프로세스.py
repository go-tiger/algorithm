def solution(priorities, location):
    answer = 0
    arr = list(range(len(priorities)))
    
    while len(priorities) != 0:
        max_value = max(priorities)
        
        if priorities[0] < max_value:
            priorities.append(priorities.pop(0))
            arr.append(arr.pop(0))
        else:
            answer += 1
            priorities.pop(0)
            if arr.pop(0) == location:
                return answer