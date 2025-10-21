from collections import Counter

def solution(k, tangerine):
    sizes_count = Counter(tangerine)
    fruits_counts = sorted(sizes_count.values(), reverse=True)
    current_sum = 0
    distinct_types_count = 0
    for count_of_type in fruits_counts:
        current_sum += count_of_type
        distinct_types_count += 1
        if current_sum >= k:
            return distinct_types_count