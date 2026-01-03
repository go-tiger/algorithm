def solution(babbling):
    answer = 0
    valid_sounds = ["aya", "ye", "woo", "ma"]
    
    for bab_word in babbling:
        has_consecutive = False
        for sound in valid_sounds:
            if (sound * 2) in bab_word:
                has_consecutive = True
                break
        
        if has_consecutive:
            continue
            
        current_bab = bab_word
        for sound in valid_sounds:
            current_bab = current_bab.replace(sound, " ")
        
        if current_bab.replace(" ", "") == "":
            answer += 1
            
    return answer