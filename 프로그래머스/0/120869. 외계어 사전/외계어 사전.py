def solution(spell, dic):
    answer = 2
    sorted_spell_str = "".join(sorted(spell))
    
    for word_in_dic in dic:
        sorted_dic_word_str = "".join(sorted(list(word_in_dic)))
        if sorted_dic_word_str == sorted_spell_str:
            answer = 1
            break      
    return answer