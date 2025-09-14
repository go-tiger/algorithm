def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        stretched_horizontal_parts = []
        for j in range(len(picture[i])):
            stretched_horizontal_parts.append(picture[i][j] * k)
        
        full_stretched_row = "".join(stretched_horizontal_parts)
        
        for _ in range(k):
            answer.append(full_stretched_row)
            
    return answer