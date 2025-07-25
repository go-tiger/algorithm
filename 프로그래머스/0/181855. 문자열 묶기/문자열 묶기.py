def solution(strArr):
    lengths = [len(s) for s in strArr]
    
    length_counts = {}
    for length in lengths:
        length_counts[length] = length_counts.get(length, 0) + 1
        
    if length_counts:
        return max(length_counts.values())
    else:
        return 0