def solution(intStrs, k, s, l):
    answer = []
    for int_str in intStrs:
        temp_str = int_str[s : s + l]
        temp_num = int(temp_str)

        if temp_num > k:
            answer.append(temp_num)          
    return answer