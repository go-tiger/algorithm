function solution(str1, str2) {
    var answer = '';
    str1 = str1.split('');
    str2 = str2.split('');
    for (let i = 0; i < str1.length; i++) {
        answer += str1[i]
        answer += str2[i]
    }
    return answer;
}