function solution(sides) {
    let answer = 0
    const max = Math.max(...sides)
    const min = Math.min(...sides)
    
    for (let i = max - min + 1; i <= max; i++) {
        answer++
    }
    
    for (let i = max + 1; i < max + min; i++) {
        answer++
    }
    return answer
}