def solution(arr):
    answer = []
    row = len(arr)
    col = len(arr[0]) if arr else 0

    if row > col:
        for i in range(row):
            new_row = list(arr[i])
            for _ in range(row - col):
                new_row.append(0)
            answer.append(new_row)
    elif row < col:
        for i in range(col):
            if i < row:
                answer.append(list(arr[i]))
            else:
                new_row = [0] * col
                answer.append(new_row)
    else:
        answer = [list(r) for r in arr]
        
    return answer