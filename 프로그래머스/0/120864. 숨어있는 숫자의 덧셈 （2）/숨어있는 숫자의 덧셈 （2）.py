import re

def solution(my_string):
    nums_str = re.findall(r'[0-9]+', my_string)
    answer = sum(int(num_s) for num_s in nums_str)
    return answer