function solution(my_string) {
    var answer = Array(52).fill(0);
    let al = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    for (let i = 0; i < my_string.length; i++) {
        answer[al.indexOf(my_string[i])]++
    }
    return answer;
}