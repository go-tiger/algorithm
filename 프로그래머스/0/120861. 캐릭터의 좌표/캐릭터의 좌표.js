function solution(keyinput, board) {
    let answer = [0, 0];
    let endX = (board[0] - 1) / 2;
    let endY = (board[1] - 1) / 2;
    
    for (let i of keyinput) {
        switch(i){
            case 'left' : if(answer[0] != -endX) answer[0]--; break;
            case 'right' : if(answer[0] != endX) answer[0]++; break;
            case 'up' : if(answer[1] != endY) answer[1]++; break;
            case 'down' : if(answer[1] != -endY) answer[1]--; break;
        }
    }
    return answer;
}