function solution(order) {
    let answer = 0;
    order.forEach((od) => {
        if (od.includes("americano")) {
            answer += 4500;
        } else if (od.includes("cafelatte")) {
            answer += 5000;
        } else if (od.includes("anything")) {
            answer += 4500;
        }
    });
    return answer;
}