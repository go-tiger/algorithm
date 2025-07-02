def solution(my_string):
    unique_chars = set(my_string)
    return "".join(dict.fromkeys(my_string))