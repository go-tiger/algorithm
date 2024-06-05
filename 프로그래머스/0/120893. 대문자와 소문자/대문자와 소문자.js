function solution(my_string) {
    var answer = [];
    
    for (let i = 0; i < my_string.length; i++) {
        if (my_string[i] === my_string[i].toUpperCase()) {
            answer.push(my_string[i].toLowerCase())
        } else {
            answer.push(my_string[i].toUpperCase())
        }
    }
    return answer.join('');
}