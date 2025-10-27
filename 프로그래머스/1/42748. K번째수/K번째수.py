def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        temp_list = array[i - 1 : j]
        temp_list.sort()
        answer.append(temp_list[k - 1])
    return answer