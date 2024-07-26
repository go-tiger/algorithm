function solution(my_string, num1, num2) {
    var answer = [...my_string];
    answer.splice(num1, 1, my_string[num2])
    answer.splice(num2, 1, my_string[num1])
    return answer.join('');
}