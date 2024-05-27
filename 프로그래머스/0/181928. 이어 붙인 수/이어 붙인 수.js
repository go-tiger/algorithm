function solution(num_list) {
    let oddStr = '';
    let evenStr = '';

    num_list.forEach(num => {
        if (num % 2 === 0) {
            evenStr += num.toString();
        } else {
            oddStr += num.toString();
        }
    });
    let oddNum = parseInt(oddStr, 10);
    let evenNum = parseInt(evenStr, 10);

    return oddNum + evenNum;
}