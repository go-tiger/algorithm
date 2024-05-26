function solution(num_list) {
    let sum = 0;
    let mul = 1;
    for (let i = 0; i < num_list.length; i++) {
        mul *= num_list[i];
        sum += num_list[i];
    }
    sum = sum * sum;
    if (mul < sum) {
        return 1;
    } 
    return 0;
}