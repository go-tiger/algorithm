def solution(numbers):
    num_str_map = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]
    for idx, str_word in enumerate(num_str_map):
        numbers = numbers.replace(str_word, str(idx))
    return int(numbers)