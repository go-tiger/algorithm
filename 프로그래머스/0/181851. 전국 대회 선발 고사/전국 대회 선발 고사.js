function solution(rank, attendance) {
    let answer = [];
    rank.unshift(0)
    attendance.unshift(0)
    for (let i = 0; i < rank.length; i++) {
        if(rank.indexOf(i) && attendance[rank.indexOf(i)]) {
            answer.push(rank.indexOf(i))
        }
    }
    return (10000 * (answer[0] - 1) ) + (100 * (answer[1] - 1) ) + (answer[2] - 1) 
}