function solution(number) {
    var answer = 0;
    for(let strNum of number) {
        answer += Number(strNum);
    }
    return answer % 9;
}