function solution(arr) {
    arr.sort((a,b) => b - a)
    let r, m, n = 0, acc = arr[0]
    for (let i = 1; i < arr.length; ++i) {
        m = acc
        n = arr[i]
        while (0 < n) {
            r = m % n
            m = n
            n = r
        }
        acc = acc * arr[i] / m
    }
    return acc;
}