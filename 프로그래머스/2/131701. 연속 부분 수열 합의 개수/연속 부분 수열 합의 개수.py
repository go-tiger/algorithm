def solution(elements):
    inbox = set()
    n = len(elements)
    for i in range(1, n + 1):
        temp_elements = elements + elements[:i-1] 
        temp_elements = elements + elements[:i]
        for k in range(n):
            current_sum = sum(temp_elements[k : k + i])
            inbox.add(current_sum)
            
    return len(inbox)
