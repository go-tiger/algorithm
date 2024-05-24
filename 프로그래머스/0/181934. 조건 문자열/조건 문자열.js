function solution(ineq, eq, n, m) {
    if (ineq === ">") {
        if (eq === "=") {
           answer = n >= m ? 1 : 0
        } else {
           answer = n > m ? 1 : 0
        }
        
    } else if (ineq === "<") {
        if (eq === "=") {
           answer = n <= m ? 1 : 0
        } else {
           answer = n < m ? 1 : 0
        }
    }
    return answer
}