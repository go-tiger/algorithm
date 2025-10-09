def solution(s):
    stack = []
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    return 0 if stack else 1