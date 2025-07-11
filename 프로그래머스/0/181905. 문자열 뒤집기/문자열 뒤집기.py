def solution(my_string, s, e):
    substring_to_reverse = my_string[s:e + 1]
    reversed_substring = substring_to_reverse[::-1]
    return my_string[:s] + reversed_substring + my_string[e + 1:]