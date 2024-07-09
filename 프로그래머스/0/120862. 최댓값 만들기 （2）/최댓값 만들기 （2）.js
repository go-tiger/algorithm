function solution(numbers) {
    numbers.sort((a, b) => a - b);
    let a = numbers[numbers.length - 1] * numbers[numbers.length - 2];
    let b = numbers[0] * numbers[1];
    return Math.max(a, b);
}