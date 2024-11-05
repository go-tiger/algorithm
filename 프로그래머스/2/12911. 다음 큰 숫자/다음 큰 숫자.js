function solution(n) {
    let arr = n.toString(2).split('')
    let cnt = arr.filter((one) => one === '1').length
    let cnt2
    while (cnt !== cnt2) {
        ++n
        cnt2 = n.toString(2).split('').filter((one)=>one==='1').length
    }
    return n
}