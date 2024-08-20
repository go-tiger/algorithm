function solution(myStr) {
    var answer = myStr.replace(/a|b|c/g , ' ').split(' ').filter((e)=> e!='');
    return answer.length == 0 ? ["EMPTY"] : answer;
}