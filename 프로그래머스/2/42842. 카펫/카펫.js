function solution(brown, yellow) {
    let answer = []
    const CARPET_SIZE = brown + yellow
    
    for (let i = 3; i < CARPET_SIZE; i++) {
        let width = CARPET_SIZE / i
        let height = i
        
        if (width < height) continue

        if ((width - 2) * (height - 2) === yellow) {
            answer[0] = width
            answer[1] = height
        }
    }
    return answer
}