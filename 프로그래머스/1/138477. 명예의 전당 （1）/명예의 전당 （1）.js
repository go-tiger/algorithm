function solution(k, score) {
    let answer = []
    let kscore = []
    for (const s of score) {
        kscore.push(s)
        kscore.sort((a, b) => a - b)
        if (kscore.length > k) {
            kscore.shift()
        }
        answer.push(kscore[0])
    }
    return answer
}