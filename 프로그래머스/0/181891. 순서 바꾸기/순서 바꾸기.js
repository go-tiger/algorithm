function solution(num_list, n) {
    let answer = num_list.slice(n, num_list.length);
    let s = num_list.slice(0, n);
    for (let i of s) {
        answer.push(i);
    }
    return answer;
}