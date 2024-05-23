function solution(number, n, m) {
    var answer = 0;
    if(number % n === 0 && number % m === 0){
        answer = 1
    }
    return answer;
}