function solution(arr, k) {
    var answer = [];
    for (i in arr) {
        if (k % 2 === 1) {
            answer.push(k * arr[i])
        } else {
            answer.push(k + arr[i])
        }
    }
    return answer;
}