def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    answer.sort()
    if answer:
        return answer
    else:
        return [-1]