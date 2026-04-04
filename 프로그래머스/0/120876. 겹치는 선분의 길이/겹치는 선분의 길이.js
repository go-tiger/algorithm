function solution(lines) {
    let arr = []; 
    const cnt = new Map();
    const set = new Set();
    
    lines.forEach(([x, y]) => {
        for(let i = x; i < y; i++) {
            arr.push(i.toString() + (i+1).toString());
        }
    });
    
    arr.forEach((v) => cnt.set(v, (cnt.get(v) || 0) + 1));
    arr.filter((v) => cnt.get(v) !== 1).forEach((v) => set.add(v));
    
    return set.size;
}