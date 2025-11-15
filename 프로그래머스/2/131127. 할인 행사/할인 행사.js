function solution(want, number, discount) {
    let numbers = [];
    let answer = 0, count = 0;
    
    for (let i = 0; i <= discount.length - 10; i++) {
        numbers = [...number];
        const stuff = discount.slice(i, i + 10);
        for (const el of stuff) {
            const idx = want.indexOf(el);
            if (idx === -1) continue;
            if (numbers[idx] > 0) {
                numbers[idx]--;
                count++;
            }
        }
        if (count === 10) answer++;
        count = 0;
    }
    return answer;
}