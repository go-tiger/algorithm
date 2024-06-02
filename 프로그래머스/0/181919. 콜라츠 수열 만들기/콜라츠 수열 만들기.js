function solution(n) {
    var answer = [];
    while (n !== 1) {
        answer.push(n);
        if (n % 2 === 0) {
            n = n / 2;
        } else {
            n = n * 3 + 1;
        }
    }
    answer.push(1);
    return answer;
}