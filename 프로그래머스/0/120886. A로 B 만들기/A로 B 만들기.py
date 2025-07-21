def solution(before, after):
    sorted_before = "".join(sorted(list(before)))
    sorted_after = "".join(sorted(list(after)))
    
    return 1 if sorted_before == sorted_after else 0