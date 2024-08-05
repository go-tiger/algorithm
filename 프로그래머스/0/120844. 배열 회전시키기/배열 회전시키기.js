function solution(numbers, direction) {  
    if (direction === 'right') {  
        const n = numbers.pop();  
        numbers.unshift(n);  
    } else {  
        const n = numbers.shift();  
        numbers.push(n);  
    }
    return numbers;  
}
