function solution(arr, k) {
    const set = new Set(arr);
    const answer = [...set].slice(0,k);
    while (answer.length !== k) {
        answer.push(-1);
    }
    return answer;
}