function solution(numbers, k) {
    let answer = 1
    for (let i = 0; i < k-1; i++) {
        answer += 2
        if (answer > numbers.length) {
            answer -= numbers.length
        }
    }
    return answer
}