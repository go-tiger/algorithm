def solution(my_string):
    answer = []
    
    for char in my_string:
        if char.isupper():
            answer.append(char.lower())
        else:
            answer.append(char.upper())
            
    return ''.join(answer)