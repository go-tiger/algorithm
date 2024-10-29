function solution(s){
    let answer = 0;

    for (let i = 0; i < s.length; i++) {
        s[i] === "(" ? answer += 1 : answer +=  -1 
        if (answer < 0) {
            break;
        }
    }
    return answer === 0 ? true : false
}