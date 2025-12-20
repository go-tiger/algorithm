from collections import Counter

def solution(topping):
    result = 0
    
    left_counts = Counter([topping[0]])
    right_counts = Counter(topping[1:])
    
    left_unique_count = len(left_counts)
    right_unique_count = len(right_counts)
    
    for i in range(1, len(topping)):
        current_topping = topping[i]
        
        right_counts[current_topping] -= 1
        
        if right_counts[current_topping] == 0:
            right_unique_count -= 1
            
        if left_counts[current_topping] == 0:
            left_unique_count += 1
        left_counts[current_topping] += 1
        
        if left_unique_count == right_unique_count:
            result += 1

    return result