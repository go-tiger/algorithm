def solution(polynomial):
    x_coeff_sum = 0
    constant_sum = 0

    terms = polynomial.split(" + ")

    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_coeff_sum += 1
            else:
                x_coeff_sum += int(term[:-1])
        else:
            constant_sum += int(term)

    result_parts = []
    if x_coeff_sum > 0:
        if x_coeff_sum == 1:
            result_parts.append('x')
        else:
            result_parts.append(f'{x_coeff_sum}x')

    if constant_sum > 0:
        result_parts.append(str(constant_sum))

    if not result_parts:
        return "0"
    
    return " + ".join(result_parts)
