import math

def solution(numer1, denom1, numer2, denom2):
    new_numer = (numer1 * denom2) + (numer2 * denom1)
    new_denom = denom1 * denom2
    common_divisor = math.gcd(new_numer, new_denom)
    return [new_numer // common_divisor, new_denom // common_divisor]
