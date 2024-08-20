function solution(strArr) {
    let answer = strArr.map((v) => v.length);
    let result = {};
    for (let i of answer) {
        result[i] = (result[i] || 0) + 1;
    }
    return Math.max(...Object.values(result));
}