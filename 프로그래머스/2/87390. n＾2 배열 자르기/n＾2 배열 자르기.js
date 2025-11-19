function solution(n, left, right) {
    let answer = [];
    for (let i = left; i <= right; i++) {
        const s = parseInt(i / n)
        const r = i % n
        answer.push(Math.max(s, r) + 1)
    }
    return answer;
}