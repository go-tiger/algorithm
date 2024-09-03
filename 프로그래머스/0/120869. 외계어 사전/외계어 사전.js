function solution(spell, dic) {
    let answer = 2;
    spell = spell.sort().join('')
    dic.forEach(a => {
        if (a.split('').sort().join('') == spell) {
            return answer = 1
        }
    })
    return answer;
}