function solution(n) {
    var answer = [];
    for(let i = 1; i <= n; i++) {
        if(n % i === 0) {
            answer.push(n / i);
        } 
    }
    return answer.length % 2 ? 1 : 2;
}