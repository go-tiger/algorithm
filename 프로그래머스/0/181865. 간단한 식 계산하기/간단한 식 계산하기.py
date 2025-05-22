def solution(binomial):
    s = binomial.split()
    a = int(s[0])
    op = s[1]
    b = int(s[2])

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b