function solution(arr, n) {
    if (arr.length % 2 === 1) {
       return arr.map((num,i) => i % 2 === 0? num + n: num)
    } else {
       return arr.map((num,i) => i % 2 === 1? num + n: num)
    }
}