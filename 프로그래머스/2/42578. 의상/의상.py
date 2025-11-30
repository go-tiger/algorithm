import collections

def solution(clothes):
    type_counts = collections.defaultdict(int)
    
    for item in clothes:
        type_ = item[1]
        type_counts[type_] += 1
        
    total_combinations = 1
    
    for count in type_counts.values():
        total_combinations *= (count + 1)
        
    return total_combinations - 1