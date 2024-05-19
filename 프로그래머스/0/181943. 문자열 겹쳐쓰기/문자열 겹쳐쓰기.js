function solution(my_string, overwrite_string, s) {
    let answer = [];
    for (let i = 0; i < my_string.length; i++) {
        answer[i] = my_string[i];
    }

    for (let i = 0; i < overwrite_string.length; i++) {
        answer[s+i] = overwrite_string[i];
    }

    return answer.join("");
}