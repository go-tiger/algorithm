function solution(my_string, queries) {
    for (let i of queries) {
        let [start, end] = i;
        let subString = my_string.substring(start, end + 1);
        subString = subString.split('').reverse().join('');
        my_string = my_string.substring(0, start) + subString + my_string.substring(end + 1);
    }
    return my_string;
}