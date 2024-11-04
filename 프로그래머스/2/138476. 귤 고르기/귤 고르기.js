function solution(k, tangerine) {
    const sizes = {}
    tangerine.forEach((it) => sizes[it] ? sizes[it]++ : sizes[it] = 1)
    
    const fruits = Object.values(sizes)
    fruits.sort((a,b) => b - a);

    let sum = 0
    let count = 0

    for (let fruit of fruits) {
        sum += fruit
        count++
        if (sum >= k) {
            return count
        }
    }
}