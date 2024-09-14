function solution(numer1, denom1, numer2, denom2) {
    let num1 = (numer1 * denom2) + (numer2 * denom1), num2 = denom1 * denom2, max = 1;

    for (let i = 1; i <= num1; i++) {
        if (num1 % i == 0 && num2 % i == 0) {
            max = i;
        }
    }
    return [num1 / max, num2 / max];
}