function solution(progresses, speeds) {
  const answer = []
  const days = progresses.map((p, i) => Math.ceil((100 - p) / speeds[i]))
  let prev = 0

  for (let i = 0; i < days.length; i++) {
    if (days[prev] < days[i]) {
      answer.push(i - prev)
      prev = i
    }
  }
  answer.push(days.length - prev)
  return answer
}