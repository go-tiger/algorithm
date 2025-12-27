function solution(n) {
    let newArr = []
    for (let i = 2; i <= n; i++) {
        newArr.push(i)
    }
    
    let prime = []
    for (let i = 2; i <= n; i++) {
        if (newArr[i] === 0) continue
        prime.push(i)
        newArr[i] = 0
        
        for (let j = i*2; j <= n; j += i) {
            if (newArr[j] === 0) continue
            newArr[j] = 0
        }
    }
    return prime.length
}
