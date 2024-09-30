function solution(arr, divisor) {
    const answer = [];
    for (let i = 0; i < arr.length; i++) {
        if (!(arr[i] % divisor)) {
            answer.push(arr[i])
        }
    }
    return answer.sort((a,b) => a-b).length ? answer : [-1];
}