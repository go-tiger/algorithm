function solution(my_string) {
    var answer = 0;
    const nums = my_string.split("");
  
    for (let i = 0; i < nums.length; i++) {
        if (Number(nums[i])) {
           answer += Number(nums[i]) 
        }
    }
    return answer;
}