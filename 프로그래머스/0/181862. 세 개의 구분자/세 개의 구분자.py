import re

def solution(myStr):
    replaced_str = re.sub(r'[abc]', ' ', myStr)
    result_list = replaced_str.split()
    
    if not result_list:
        return ["EMPTY"]
    else:
        return result_list