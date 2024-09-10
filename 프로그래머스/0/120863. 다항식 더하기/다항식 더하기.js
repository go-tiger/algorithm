function solution(polynomial) {
    const arr = polynomial.split(" + ");
    const x = [], n = [];

    arr.forEach((v) => v.includes("x") ? x.push(v) : n.push(v));

    const nOp = x.filter((v) => v.match(/\dx/g)).map((v) => v.substr(0, v.length - 1));
    const sum1 = nOp.reduce((a, c) => a + Number(c), 0);

    const sum2 = x.length - nOp.length;

    const sum3 = n.reduce((a, c) => a + Number(c), 0);

    if (polynomial === "x") {
        return "x";
    } else if (sum3 === 0) {
        return (sum1 + sum2) + "x"
    } else {
        if (x.length === 0) {
            return sum3 + "";
        }
        else if ((sum1 + sum2) === 1) {
            return "x" + " + " + sum3;
        }
        else {
            return (sum1 + sum2) + "x" + " + " + sum3;
        }
    }
}