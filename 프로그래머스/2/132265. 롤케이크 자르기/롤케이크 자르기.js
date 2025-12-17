function solution(topping) {
    let result = 0
    let [lCnt, rCnt] = [1, 0]
    let [lArr, rArr] = [Array(topping.length).fill(0), Array(topping.length).fill(0)]
	lArr[topping[0]] += 1
    for (let i = 1; i < topping.length; i += 1) {
        if (!rArr[topping[i]]) rCnt += 1
        rArr[topping[i]] += 1
    }
    for (let i = 1; i < topping.length; i += 1) {
        if (!lArr[topping[i]]) {
            lArr[topping[i]] += 1
            lCnt += 1
        }
        if (!(rArr[topping[i]] -= 1)) rCnt -= 1
        if (lCnt === rCnt) result += 1
    }
    return result
}