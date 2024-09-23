function solution(n) {
    let answer = 0;
    let num = Math.sqrt(n)
    
    if (num % 1 === 0) {
        answer += Math.pow(num + 1, 2)
    } else {
        return -1
    }
    return answer;
}