function solution(my_string, n) {
    return [...my_string].map(s => s.repeat(n)).join("");
}