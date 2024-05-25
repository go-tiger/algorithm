function solution(a, d, included) {
  let answer = 0;
  included.map((item, index) => {
    if (item) {
      answer += a + (d * (index));
    }
  });
  return answer;
}