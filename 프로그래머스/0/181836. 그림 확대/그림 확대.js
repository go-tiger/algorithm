function solution(picture, k) {
    let answer = [];
    for (let i = 0; i < picture.length; i++) {
        let stretch = []
        for (let j = 0; j < picture[i].length; j++) {
            stretch.push(picture[i][j].repeat(k))
        }
        for (let j = 0; j < k; j++) {
         answer.push(stretch.join(''))   
        }
    }
    return answer;
}