function solution(a, b) {
    var answer = 0;
    answer = Math.max(Number(`${a}${b}`), Number(`${b}${a}`))
    return answer;
}