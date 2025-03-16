import re

def solution(str1, str2):
    return 1 if re.search(re.escape(str2), str1) else 2