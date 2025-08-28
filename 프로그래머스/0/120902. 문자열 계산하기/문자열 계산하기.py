def solution(my_string):
    arr = my_string.split()
    answer = int(arr[0])
    for i in range(1, len(arr), 2):
        answer += int(arr[i] + arr[i+1])
    return answer