function solution(hp) {
    let antG = Math.floor(hp / 5)
    let antS = Math.floor((hp - antG * 5) / 3)
    let antI = hp - antG * 5 - antS * 3

    return antG + antS + antI;
}