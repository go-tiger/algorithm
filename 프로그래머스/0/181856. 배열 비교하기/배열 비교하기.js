function solution(arr1, arr2) {
    const arr1Sum = arr1.reduce((acc, cur) => acc + cur, 0);
    const arr2Sum = arr2.reduce((acc, cur) => acc + cur, 0);

    if (arr1.length === arr2.length) {
        if (arr1Sum > arr2Sum) {
            return 1;
        } else if (arr2Sum > arr1Sum) {
            return -1;
        } else {
            return 0;
        }
    }

    return arr1.length > arr2.length ? 1 : -1;
}