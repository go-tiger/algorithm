function solution(num_list) {
    let answer = num_list
    let last = num_list[num_list.length-1] 
    let last2 = num_list[num_list.length-2]
    if(last > last2) {
       answer.push(last-last2)
    } else {
        answer.push(last*2)
    }
  return answer
}