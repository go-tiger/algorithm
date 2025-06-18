def solution(age):
    char = 'abcdefghij'
    return ''.join(char[int(digit)] for digit in str(age))