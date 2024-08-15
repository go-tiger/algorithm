function solution(i, j, k) {
    var answer = 0;
    for (let start = i; start <= j; start++) {
        String(start).split("").forEach(el => el.includes(k) && answer++);
    }
    return answer;
}