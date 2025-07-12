def solution(myString, pat):
    last_index_of_pat = myString.rfind(pat)
    return myString[:last_index_of_pat] + pat