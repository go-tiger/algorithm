function solution(n) {
    let fi = [1, 1]
    for (let i = 2; i <= n; i++) {
        fi[i] = (fi[i - 1] + fi[i - 2]) % 1234567
    }
    return fi[n]
}