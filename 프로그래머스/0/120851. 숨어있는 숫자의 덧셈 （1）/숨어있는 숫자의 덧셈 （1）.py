def solution(my_string):
    answer = 0
    nums = list(my_string)
    
    for char in nums:
        if char.isdigit():
            answer += int(char)
            
    return answer