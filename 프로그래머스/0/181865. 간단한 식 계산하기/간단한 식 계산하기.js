function solution(binomial) {
    const s = binomial.split(" ");
    const a = parseInt(s[0]);
    const b = parseInt(s[2]);

    switch(s[1]) {
        case "+" :
            return a + b;
        case "-" :
            return a - b;
        case "*" :
            return a * b;
    }
}