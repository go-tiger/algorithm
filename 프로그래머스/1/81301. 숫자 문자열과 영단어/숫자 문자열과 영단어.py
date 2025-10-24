def solution(s):
    numbers_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer_str = s
    for i in range(len(numbers_str)):
        answer_str = answer_str.replace(numbers_str[i], str(i))
    return int(answer_str)