import json

def solution(s):
    result = []

    s_processed = s.replace('{', '[').replace('}', ']')
    tuples = json.loads(s_processed)
    tuples.sort(key=len)

    seen_elements = set()

    for current_tuple in tuples:
        for element in current_tuple:
            if element not in seen_elements:
                seen_elements.add(element)
                result.append(element)
    return result