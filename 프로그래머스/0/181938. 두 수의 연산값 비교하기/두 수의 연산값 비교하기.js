function solution(a, b) {
    const ab = String(a) + String(b)
    const ab2 = 2*a*b
    
    answer = Math.max(Number(ab), Number(ab2))
    return answer;
}