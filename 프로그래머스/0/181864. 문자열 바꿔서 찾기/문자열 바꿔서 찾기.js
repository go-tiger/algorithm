function solution(myString, pat) {
    let answer = "";
    myString.split("").map(x => {
        if (x === "A") { 
            answer += "B";
        } else {
            answer += "A";
        };
    })
    return answer.includes(pat) ? 1 : 0;;
}