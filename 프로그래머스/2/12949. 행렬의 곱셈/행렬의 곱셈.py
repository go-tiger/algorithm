def solution(arr1, arr2):
    new_arr = []

    for i in range(len(arr1)):
        row_result = []
        for j in range(len(arr2[0])):
            element_sum = 0
            for k in range(len(arr2)):
                element_sum += arr1[i][k] * arr2[k][j]
            row_result.append(element_sum)
        new_arr.append(row_result)
    return new_arr