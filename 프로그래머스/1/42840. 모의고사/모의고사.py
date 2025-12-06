def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt_array = [0, 0, 0]
    
    length1 = len(person1)
    length2 = len(person2)
    length3 = len(person3)
    
    for i in range(len(answers)):
        if person1[i % length1] == answers[i]:
            cnt_array[0] += 1
        if person2[i % length2] == answers[i]:
            cnt_array[1] += 1
        if person3[i % length3] == answers[i]:
            cnt_array[2] += 1
            
    max_value = max(cnt_array)
    
    result = []
    for idx, score in enumerate(cnt_array):
        if score == max_value:
            result.append(idx + 1)
            
    return result