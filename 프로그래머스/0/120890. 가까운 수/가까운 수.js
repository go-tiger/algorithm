function solution(array, n) {
    array.sort((x,y) => x - y)
    let differ = Infinity;
    let answer = 0;
    for(let i of array) { 
        if (Math.abs(n - i) < differ) {  
        differ = Math.abs(n - i) 
        answer = i 
        }
    }
    return answer; 
}