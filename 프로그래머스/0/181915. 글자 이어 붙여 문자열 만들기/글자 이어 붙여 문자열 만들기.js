function solution(my_string, index_list) {
    var answer = '';
    index_list.map((i) => {
        answer += my_string[i]
    })
    return answer;
}