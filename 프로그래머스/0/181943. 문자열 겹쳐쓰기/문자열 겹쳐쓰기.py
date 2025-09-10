def solution(my_string, overwrite_string, s):
    my_string_list = list(my_string)
    for i in range(len(overwrite_string)):
        my_string_list[s + i] = overwrite_string[i]
    return "".join(my_string_list)