def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        key1 = format(arr1[i], 'b').zfill(n)
        key2 = format(arr2[i], 'b').zfill(n)
        password_row = ''
        for j in range(n):
            if key1[j] == '1' or key2[j] == '1':
                password_row += '#'
            else:
                password_row += ' '
        answer.append(password_row)
    return answer