function solution(my_string, s, e) {
    let answer = '';
    const str = my_string.substring(s, e + 1);
    const nStr = str.split('').reverse().join('');

    answer = my_string.replace(str, nStr);
    return answer;
}