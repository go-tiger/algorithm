function solution(my_string) {
    var answer = 0;
    const nums = my_string.match(/[0-9]+/g);
    if (nums === null) {
        return answer;
    }

    for (let i = 0; i < nums.length; i++) {
        answer += Number(nums[i])
    }
    return answer;
}