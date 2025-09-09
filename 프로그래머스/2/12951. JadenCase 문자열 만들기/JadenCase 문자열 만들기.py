def solution(s):
    words = s.lower().split(" ")
    processed_words = []
    for word in words:
        if word:
            processed_words.append(word[0].upper() + word[1:])
        else:
            processed_words.append("")
    return " ".join(processed_words)