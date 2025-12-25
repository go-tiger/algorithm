function solution(nums) {
    let answer = 0
    const memo = {}
    
    for (let first = 0; first < nums.length - 2; first++) {
        for (let second = first + 1; second < nums.length - 1; second++ ) {
            for (let third = second + 1; third < nums.length; third++) {
                const sum = nums[first] + nums[second] + nums[third]
                if (memo[sum] || isPrime(sum)) {
                    answer += 1
                    if (memo[sum] === undefined) {
                        memo[sum] = true
                    }
                }
            }
        }
    }
    return answer
}

function isPrime(num) {
    if (num === 2) return true
    if (num % 2 === 0) return false
    
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0) {
            return false
        }
    }
    return true
}