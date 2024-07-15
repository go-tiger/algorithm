function solution(myString, pat) {
    const regex = new RegExp(pat, "gi");
    return +regex.test(myString);
}