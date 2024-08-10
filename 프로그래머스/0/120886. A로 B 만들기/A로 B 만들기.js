function solution(before, after) {
    before = [...before].sort().join('');
    after = [...after].sort().join('');
    return before === after ? 1 : 0; 
}