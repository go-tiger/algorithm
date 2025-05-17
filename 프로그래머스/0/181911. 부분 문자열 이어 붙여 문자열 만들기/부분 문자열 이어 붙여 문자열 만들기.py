def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        start, end = parts[i]
        answer += my_strings[i][start:end+1]
    return answer