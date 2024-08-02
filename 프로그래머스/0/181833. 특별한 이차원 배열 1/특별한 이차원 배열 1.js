function solution(n) {
    const arr = Array.from(Array(n), () => new Array(n))
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            arr[i][j] = i === j ? 1 : 0;
        }
    }
    return arr;
}