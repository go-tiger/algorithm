function solution(n) {
    let arr = new Array(n + 1).fill(0);
    
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= i; j++) {
            if (i % j === 0) {
                arr[i]++
            };
        }
    }
    return arr.filter((v) => v >= 3).length;
}