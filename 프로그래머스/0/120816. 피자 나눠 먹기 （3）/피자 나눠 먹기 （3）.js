function solution(slice, n) {
    var answer = 0;
    while (n > slice * answer) {
        answer++
    }
    return answer;
}