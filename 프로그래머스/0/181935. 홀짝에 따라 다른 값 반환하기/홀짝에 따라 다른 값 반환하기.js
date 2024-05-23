function solution(n) {
    let answer = 0;

    if (n % 2 !== 0) {
        for (let i = 1; i <= n; i += 2) {
            answer += i;
        }
    } else {
        for (let i = 2; i <= n; i += 2) {
            answer += i * i;
        }
    }
    return answer;
}