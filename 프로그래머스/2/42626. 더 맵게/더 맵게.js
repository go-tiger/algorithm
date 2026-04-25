function solution(scoville, K) {
    let heap = new MinHeap();
    let answer = 0;
    
    for (const dish of scoville) {
        heap.push(dish);
    }
    
    while (heap.size() >= 2 && heap.peek() < K) {
        const first = heap.pop();
        const second = heap.pop();
        const newDish = first + (second * 2);
        heap.push(newDish);
        answer++;
    }
    
    return heap.peek() >= K ? answer : -1;
}

class MinHeap {
    constructor() {
        this.heap = [];
    }
    
    size() {
        return this.heap.length;
    }
    
    push(value) {
        this.heap.push(value);
        
        let curIndex = this.heap.length - 1;
        let parIndex = Math.floor((curIndex - 1) / 2);
        
        while (curIndex > 0 && this.heap[curIndex] < this.heap[parIndex]) {
            [this.heap[parIndex], this.heap[curIndex]] = [this.heap[curIndex], this.heap[parIndex]];
            
            curIndex = parIndex;
            parIndex = Math.floor((curIndex - 1) / 2);
        }
    }
    
    pop() {
        if (this.size() === 0) return null;
        if (this.size() === 1) return this.heap.pop();
        
        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        
        let curIndex = 0;
        let left = 1;
        let right = 2;
        
        while (
            this.heap[curIndex] > this.heap[left] || this.heap[curIndex] > this.heap[right]
        ) {
            if (this.heap[left] > this.heap[right]) {
                [this.heap[right], this.heap[curIndex]] = [this.heap[curIndex], this.heap[right]];
                curIndex = right;
            }
            else {
                [this.heap[left], this.heap[curIndex]] = [this.heap[curIndex], this.heap[left]];
                curIndex = left;
            }
            left = curIndex * 2 + 1;
            right = curIndex * 2 + 2;
        }
        
        return min;
    }
    
    peek() {
        return this.heap[0];
    }
}