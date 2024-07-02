function solution(myString, pat) {
    const lastIndexOf = myString.lastIndexOf(pat);
    return myString.slice(0, lastIndexOf) + pat;
}