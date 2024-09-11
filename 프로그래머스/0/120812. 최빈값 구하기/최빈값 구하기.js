function solution(array) {
    let answer = 0;
    let res = new Array(1000);
    res.fill(0);

    for (let i = 0; i < array.length; i++) {
        res[array[i]] += 1;
    }

    let max = Math.max(...res);
    let cnt = 0;
    for (let i = 0; i < res.length; i++) {
        if (max === res[i]) {
            answer = i;
            cnt++;
        }
        if (cnt >= 2) {
            return -1;
        }
    }
    return answer;
}  