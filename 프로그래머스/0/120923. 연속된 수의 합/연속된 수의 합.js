function solution(num, total) {
    let answer = [];
    
    let sum = num * (1 + num) / 2;
    let start = (total - sum) / num;

    for (let i = 0; i < num; i++)  {
        answer[i] = start + i + 1;
    }
    return answer;
}