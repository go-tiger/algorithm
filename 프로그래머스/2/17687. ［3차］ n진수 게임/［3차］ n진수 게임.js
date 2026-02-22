function solution(n, t, m, p) {
    let sequence = ""
    let number = 0
    
    while (sequence.length < t * m) {
        sequence += number.toString(n).toUpperCase()
        number++
    }
    let answer = ""
    
    for (let i = p - 1; i < t * m; i += m) {
        answer += sequence[i]
    }
    return answer
}
