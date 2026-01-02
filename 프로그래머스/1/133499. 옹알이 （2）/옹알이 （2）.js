function solution(babbling) {
    let answer = 0
    let arr = ["aya", "ye", "woo", "ma"]
    
    for (let i = 0; i < babbling.length; i++) {
        let bab = babbling[i]
        
        for (let j=0; j < arr.length; j++) {
            if (bab.includes(arr[j].repeat(2))) {
                break
            }
            bab = bab.split(arr[j]).join(" ")
        }
        if (bab.split(" ").join("").length === 0) {
            answer ++
        }
    }
    return answer
}