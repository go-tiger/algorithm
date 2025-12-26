import math

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    memo = {}
    
    for first in range(len(nums) - 2):
        for second in range(first + 1, len(nums) - 1):
            for third in range(second + 1, len(nums)):
                current_sum = nums[first] + nums[second] + nums[third]
                if current_sum in memo or is_prime(current_sum):
                    answer += 1
                    if current_sum not in memo:
                        memo[current_sum] = True
    return answer