def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)