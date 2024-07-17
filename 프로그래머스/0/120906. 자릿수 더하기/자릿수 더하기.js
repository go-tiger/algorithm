function solution(n) {
    let answer = 0;
    n = n.toString();
    for (let i of n) {
        answer += Number(i);
    }
    return answer;
}