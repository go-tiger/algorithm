function solution(num_list) {
    let sumEven = 0;
    let sumOdd = 0;
    for (let i = 0; i < num_list.length; i++) {
        if (i % 2 == 0) {
            sumEven += num_list[i];
        } else {
            sumOdd += num_list[i];
        }
    }
    return Math.max(sumEven, sumOdd);
}