def solution(quiz):
    answer = []
    for q in quiz:
        parts = q.split('=')
        expression = parts[0].strip()
        expected_result = int(parts[1].strip())
        
        calculated_result = eval(expression)
        
        if calculated_result == expected_result:
            answer.append("O")
        else:
            answer.append("X")
    return answer