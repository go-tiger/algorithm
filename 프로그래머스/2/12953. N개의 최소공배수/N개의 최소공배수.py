import math

def solution(arr):
    arr.sort(reverse=True)
    
    if not arr:
        return 0

    acc = arr[0]

    for i in range(1, len(arr)):
        m_val = acc
        n_val = arr[i]
        gcd_val = math.gcd(m_val, n_val)
        acc = (acc * arr[i]) // gcd_val
    return acc