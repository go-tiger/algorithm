function solution(N, stages) {
    let answer = []
    for (let i = 1; i <= N; i++) {
        let top = stages.filter((stage) => stage === i).length
        let bottom = stages.filter((stage) => stage >= i).length

        if (bottom === 0) {
            answer.push({ stageNumber: i, failRate: 0 })
        } else {
            answer.push({ stageNumber: i, failRate: top / bottom })
        }
    }

    return answer
        .sort((a, b) => b.failRate === a.failRate ? a.stageNumber - b.stageNumber : b.failRate - a.failRate)
        .map((stage) => stage.stageNumber);
}