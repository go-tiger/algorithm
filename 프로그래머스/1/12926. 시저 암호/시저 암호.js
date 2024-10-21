function solution(s, n) {
    let answer = ''
    
    s = s.split('')
    
    s.map((str) => {
        let ascii = str.charCodeAt() + n;
        if (str === ' ') {
            answer += ' '
        } else {
            if (str === str.toLowerCase() && ascii > 122) {
                ascii -= 26
            } else if (str === str.toUpperCase() && ascii > 90) {
                ascii -= 26
            }
            answer += String.fromCharCode(ascii)
        }
    })
    return answer
}