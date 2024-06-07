function solution(n, k) {
    var answer = 0;
    if (n >= 10) {
       k -= Math.floor(n/10);
    }
    return answer = n*12000+k*2000;
}