def solution(s, n):
    answer_chars = []
    
    for char in s:
        if char == ' ':
            answer_chars.append(' ')
        elif char.islower():
            start_ascii = ord('a')
            shifted_ascii = (ord(char) - start_ascii + n) % 26 + start_ascii
            answer_chars.append(chr(shifted_ascii))
        elif char.isupper():
            start_ascii = ord('A')
            shifted_ascii = (ord(char) - start_ascii + n) % 26 + start_ascii
            answer_chars.append(chr(shifted_ascii))
            
    return "".join(answer_chars)