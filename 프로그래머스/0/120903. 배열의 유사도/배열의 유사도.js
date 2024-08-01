function solution(s1, s2) {
    return s1.filter((e) => s2.includes(e)).length;
}