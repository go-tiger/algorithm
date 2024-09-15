function solution(a, b, c, d) {
    const diceNumbers = [a, b, c, d];

    if (new Set(diceNumbers).size === 1) {
        return 1111 * a;
    }

    if (new Set(diceNumbers).size === 2) {
        const [p, q] = [...new Set(diceNumbers)];
        let count = 0;
        for (let i = 0; i < diceNumbers.length; i++) {
            for (let j = i + 1; j < diceNumbers.length; j++) {
                if (diceNumbers[i] === diceNumbers[j]) {
                    count++;
                }
            }
        }

        if (count === 3) {
            let pCount = 0, qCount = 0;

            diceNumbers.forEach((n) => {
                n === p ? pCount++ : qCount++;
            });
            return pCount > qCount ? Math.pow(10 * p + q, 2) : Math.pow(10 * q + p, 2);
        } else if (count === 2) {
            return (p + q) * Math.abs(p - q);
        }
    }

    if (new Set(diceNumbers).size === 3) {
        const [p, q, r] = [...new Set(diceNumbers)];
        let pCount = 0, qCount = 0;

        diceNumbers.forEach((n) => {
            n === p && pCount++;
            n === q && qCount++;
        });

        if (pCount === 2) {
            return q * r;
        } else if (qCount === 2) {
            return p * r;
        } else {
            return p * q;
        }
    }
    return Math.min(...diceNumbers);
}