function solution(arr, query) {
    let answer = [...arr]
    query.forEach((v,i) => {
        if (i % 2 === 0) {
            answer.splice(query[i] + 1)
        } else {
            answer.splice(0, query[i])
        }
    })
    return answer
}