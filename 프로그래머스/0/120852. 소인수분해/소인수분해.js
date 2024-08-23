function solution(n) {
    var answer = [];
    for (let i = 2; i <= n; i++) {
        while (n % i === 0) {
            n = n / i
            if (n % i !== 0) {
                answer.push(i)
            }
        }
    }
    return answer;
}