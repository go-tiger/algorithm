def solution(s):
    answer_words = []
    words = s.split(' ')
    for word in words:
        transformed_word_chars = []
        for j, char in enumerate(word):
            if j % 2 == 0:
                transformed_word_chars.append(char.upper())
            else:
                transformed_word_chars.append(char.lower())
        answer_words.append("".join(transformed_word_chars))
    return " ".join(answer_words)