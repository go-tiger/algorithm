def solution(s):
    answer = 0
    
    if len(s) % 2 != 0:
        return 0
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]
        stack = []
        is_current_rotation_correct = True
        
        for char in rotated_s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                if not stack:
                    is_current_rotation_correct = False
                    break
                opening_bracket = stack.pop()
                if opening_bracket != bracket_map[char]:
                    is_current_rotation_correct = False
                    break
        if is_current_rotation_correct and not stack:
            answer += 1
    return answer