import collections

def solution(a, b, c, d):
    dice_numbers = [a, b, c, d]
    counts = collections.Counter(dice_numbers)
    num_unique = len(counts)
    if num_unique == 1:
        return 1111 * a
    elif num_unique == 2:
        items = counts.most_common()
        if items[0][1] == 3:
            p = items[0][0]
            q = items[1][0]
            return (10 * p + q) ** 2
        else:
            p = items[0][0]
            q = items[1][0]
            return (p + q) * abs(p - q)
    elif num_unique == 3:
        single_numbers = [k for k, v in counts.items() if v == 1]
        return single_numbers[0] * single_numbers[1]
    else:
        return min(dice_numbers)