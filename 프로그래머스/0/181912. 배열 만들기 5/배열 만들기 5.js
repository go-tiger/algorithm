function solution(intStrs, k, s, l) {
    let answer = [];
    for (let i = 0; i< intStrs.length; i++) {
        let temp = parseInt(intStrs[i].slice(s, s + l));
        if (temp > k) {
            answer.push(temp);
        }
    }
    return answer;
}