function solution(arr) {
    let answer = [];
    for (let i = 0; i < arr.length; i++) {
        if (answer[answer.length - 1] === arr[i]) {
            answer.pop()
        } else {
            answer.push(arr[i])
        }
    }
    return answer.length === 0 ? [-1] : answer;
}