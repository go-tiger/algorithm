def solution(s):
    answer = 0
    arr = s.split(' ')
    for i in range(len(arr)):
        if arr[i] != 'Z':
            answer += int(arr[i])
        else:
            answer -= int(arr[i-1])
    return answer