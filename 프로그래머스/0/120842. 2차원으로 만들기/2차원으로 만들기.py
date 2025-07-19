import math

def solution(num_list, n):
    answer = []
    num_chunks = math.ceil(len(num_list) / n)

    for i in range(num_chunks):
        start_index = i * n
        end_index = (i * n) + n
        answer.append(num_list[start_index:end_index])
    return answer