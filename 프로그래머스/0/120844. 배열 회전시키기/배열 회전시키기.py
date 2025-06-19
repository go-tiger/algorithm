def solution(numbers, direction):
    if direction == 'right':
        n = numbers.pop()
        numbers.insert(0, n)
    else:
        n = numbers.pop(0)
        numbers.append(n)
    return numbers