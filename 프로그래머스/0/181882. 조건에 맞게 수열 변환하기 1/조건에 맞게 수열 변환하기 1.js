function solution(arr) {
    var answer = [];
    for (i of arr) {
        if (50 <= i && i % 2 === 0) {
            answer.push(i / 2)
        } else if (50 > i && i % 2 === 1) {
            answer.push(i * 2)
        } else {
            answer.push(i)
        }
    }
    return answer;
}