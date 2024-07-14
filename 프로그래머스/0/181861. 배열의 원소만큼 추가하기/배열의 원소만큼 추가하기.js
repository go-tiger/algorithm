function solution(arr) {
    var answer = [];
    for (let s of arr) {
        for (let i = 0; i < s; i++) {
            answer.push(s);
        }
    }
    return answer;
}