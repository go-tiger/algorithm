function solution(a, b, n) {
    let answer = 0;
    while (n >= a) {
        const newBottles = Math.floor(n / a) * b;
        answer += newBottles;
        n = newBottles + (n % a);
    }
    return answer;
}