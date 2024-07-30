function solution(n, t) {
    for (let i = 1; i < t + 1; i++) {
        n *= 2;
    }
    return n;
}