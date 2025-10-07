def solution(A, B):
    if A == B:
        return 0
    n = len(A)
    current_A = list(A)
    for i in range(1, n + 1):
        last_char = current_A.pop()
        current_A.insert(0, last_char)
        
        if "".join(current_A) == B:
            return i
    return -1