function solution(myString, pat) {
    var answer = 0;
    for (let i = myString.length + 1 - pat.length; i >= 0; i--) {
        if (pat === myString.substring(i, i + pat.length)) {
            answer++;
        }
    }
    return answer;
}