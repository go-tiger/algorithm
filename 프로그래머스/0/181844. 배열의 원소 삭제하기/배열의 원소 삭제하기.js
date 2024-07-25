function solution(arr, delete_list) {
    return arr.filter((i) => !delete_list.includes(i));
}