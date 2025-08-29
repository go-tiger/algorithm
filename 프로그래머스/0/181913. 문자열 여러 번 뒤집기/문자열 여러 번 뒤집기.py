def solution(my_string, queries):
    my_string_list = list(my_string)
    
    for query in queries:
        start, end = query
        sub_list = my_string_list[start : end + 1]
        sub_list.reverse()
        my_string_list[start : end + 1] = sub_list
    return "".join(my_string_list)