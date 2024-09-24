function solution(n)
{
    return String(n).split('').reduce((acc, cur) => +acc + +cur, 0);
}