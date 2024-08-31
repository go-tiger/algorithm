function solution(balls, share) {
    let answer = 1;
    while (share) {
        answer *= balls / share;
        balls--;
        share--;
    }
    return Math.round(answer);
}