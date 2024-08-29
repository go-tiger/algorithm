function solution(numbers) {
    let numStr = [ "zero", "one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine" ];

    numStr.forEach((str, idx) => {
        numbers = numbers.replaceAll(str, idx);
    });
    return Number(numbers);
}