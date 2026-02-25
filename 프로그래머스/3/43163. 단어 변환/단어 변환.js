function solution(begin, target, words) {
    let answer = 51

    if (words.includes(target)) {
        searchWords(begin, [], 0);
    }

    function searchWords(curWord, visited, count) {
        if (curWord === target) {
            answer = Math.min(answer, count)
            return
        }

        for (let i = 0; i < words.length; i++) {
            if (visited[i] !== true && checkNextWord(curWord, words[i])) {
                visited[i] = true
                searchWords(words[i], visited, count+1)
                visited[i] = false
            }
        }
    }

    function checkNextWord(cur, next) {
        let differentWords = 0

        for (let i = 0; i < cur.length; i++) {
            if (cur[i] !== next[i]) {
                differentWords++
            }
        }
        return differentWords === 1 ? true : false
    }
    return answer === 51 ? 0 : answer
}
