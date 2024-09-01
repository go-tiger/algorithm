function solution(arr) {
    let answer = [];
    const row = arr.length;
    const col = arr[0].length;
    
    if (row > col) {
        for (let i = 0; i < row; i += 1) {
            const newArr = [...arr[i]];
            for (let j = col; j < row; j += 1) {
                newArr.push(0);
            }
            answer.push(newArr);
        }
    } else if (row < col) {
        for (let i = 0; i < col; i += 1) {
            if (i < row) {
                answer.push(arr[i]);
            } else {
                const newArr = Array(col).fill(0);
                answer.push(newArr);
            }
        }
    } else {
        answer = arr;
    }
    return answer;
}