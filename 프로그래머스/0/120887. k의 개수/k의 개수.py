def solution(i, j, k):
    answer = 0
    k_str = str(k)

    for num in range(i, j + 1):
        for digit_char in str(num):
            if digit_char == k_str:
                answer += 1
    return answer