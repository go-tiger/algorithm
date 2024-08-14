function solution(num_list, n) {
    let answer = []
    for (let i = 0; i < num_list.length/n; i++) {
        answer.push(num_list.slice(i*n , i*n+n));
    }
    return answer  
}
