def solution(n, words):
    seen_words = set()
    for i, word in enumerate(words):
        player_num = (i % n) + 1
        turn_num = (i // n) + 1
        if i > 0:
            last_char_of_previous_word = words[i - 1][-1]
            if word[0] != last_char_of_previous_word:
                return [player_num, turn_num]
        if word in seen_words:
            return [player_num, turn_num]
        seen_words.add(word)     
    return [0, 0]