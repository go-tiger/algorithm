function solution(a, b) {
    let answer = 0;
    let add = Math.min(a,b);
    for (let i = 0; i < Math.abs(b - a) + 1; i++) {
        answer += add;
        add++;
    }
    return answer;
}