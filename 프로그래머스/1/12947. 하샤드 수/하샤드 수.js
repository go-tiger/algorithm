function solution(x) {
    let num = String(x);
    let result = 0;
    for (let i = 0;  i < num.length; i++) {
        result += Number(num[i]);
    }
    return x % result === 0 ? true : false ;
}