function solution(a, b) {
    let answer = new Date(2016, (a - 1), b)
    return answer.toString().slice(0, 3).toUpperCase()
}