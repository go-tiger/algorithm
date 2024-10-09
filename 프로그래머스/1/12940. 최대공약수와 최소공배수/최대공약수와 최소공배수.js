function solution(n, m) {
    let answer = [];
    let a = Math.min(n, m)
    let b = Math.max(n, m)
    
    for (let i = a; i >= 1; i--) {
        if (a % i == 0 && b % i == 0) {
            return [i, (a * b / i)]
        }
    }
    return answer;
}