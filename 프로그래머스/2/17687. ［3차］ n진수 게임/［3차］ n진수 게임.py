def solution(n, t, m, p):
    def convert_to_base(num, base):
        digits = "0123456789ABCDEF"
        if num == 0:
            return "0"
        result = ""
        while num > 0:
            result = digits[num % base] + result
            num //= base
        return result

    sequence = ""
    num = 0

    while len(sequence) < t * m:
        sequence += convert_to_base(num, n)
        num += 1

    return ''.join(sequence[i] for i in range(p - 1, t * m, m))