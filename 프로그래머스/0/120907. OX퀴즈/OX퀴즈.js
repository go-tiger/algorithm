function solution(quiz) {
    const answer = quiz.map((v) => v.replace("=", "=="));
    return answer.map((v) => eval(v) ? "O" : "X");
}