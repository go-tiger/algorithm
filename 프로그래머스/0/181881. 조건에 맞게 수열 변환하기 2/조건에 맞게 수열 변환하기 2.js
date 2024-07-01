function solution(arr) {
    let answer = arr.slice();
    let count = 0;

    while (true) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] >= 50 && arr[i] % 2 === 0) {
                arr[i] /= 2;
            } else if (arr[i] < 50 && arr[i] % 2 !== 0) {
                arr[i] = arr[i] * 2 + 1;
            }
        }

        if (JSON.stringify(arr) === JSON.stringify(answer)) {
            break;
        }
        answer = arr.slice();

        count++;
    }
    return count;
}
