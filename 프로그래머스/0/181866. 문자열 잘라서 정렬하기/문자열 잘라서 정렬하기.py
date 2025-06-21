def solution(myString):
    parts = myString.split('x')
    filtered_parts = [part for part in parts if part != '']
    return sorted(filtered_parts)