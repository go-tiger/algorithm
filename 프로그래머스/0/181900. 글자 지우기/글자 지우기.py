def solution(my_string, indices):
    answer = ''
    indices_set = set(indices)
    
    for i in range(len(my_string)):
        if i not in indices_set:
            answer += my_string[i]
    return answer