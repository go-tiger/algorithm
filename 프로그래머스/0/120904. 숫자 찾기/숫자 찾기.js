function solution(num, k) {
    var answer = num.toString().indexOf(k) + 1;
    return answer ? answer : -1;
}