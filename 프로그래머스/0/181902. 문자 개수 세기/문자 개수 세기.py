def solution(my_string):
    answer = [0] * 52
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for char in my_string:
        index = al.index(char)
        answer[index] += 1
    return answer