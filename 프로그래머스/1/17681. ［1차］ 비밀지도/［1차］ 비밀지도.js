function solution(n, arr1, arr2) {
    let answer = []
    for (let i = 0; i < n; i++) {
        let key1 = arr1[i].toString(2).padStart(n, 0)
        let key2 = arr2[i].toString(2).padStart(n, 0)
        let password = ''
        for (let j = 0; j < n; j++) {
            if (key1[j] === '1' || key2[j] === '1') password += '#'
            else password += ' '
        }
        answer.push(password)
    }
    return answer
}