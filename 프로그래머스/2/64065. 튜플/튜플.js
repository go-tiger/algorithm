function solution(s) {
  const result = []

  const tuples = JSON.parse(s.replace(/{/g, "[").replace(/}/g, "]")).sort(
    (a, b) => a.length - b.length
  );

  const set = new Set()

  for (let tuple of tuples) {
    for (let v of tuple) {
      if (!set.has(v)) {
        set.add(v)
        result.push(v)
      }
    }
  }
  return result
}