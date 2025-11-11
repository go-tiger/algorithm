from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dict = {w: n for w, n in zip(want, number)}
    for i in range(len(discount) - 9): 
        current_discount_slice = discount[i : i + 10]
        current_discount_counts = Counter(current_discount_slice)
        can_buy_all = True
        for item, required_count in want_dict.items():
            if current_discount_counts.get(item, 0) < required_count:
                can_buy_all = False
                break
        if can_buy_all:
            answer += 1        
    return answer