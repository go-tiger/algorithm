def solution(word):
    dictionary = []
    vowels = ["A", "E", "I", "O", "U"]
    
    def generate_words(current_word):
        if len(current_word) == 5:
            return
        
        for vowel in vowels:
            new_word = current_word + vowel
            dictionary.append(new_word)
            generate_words(new_word)
            
    generate_words("")
    return dictionary.index(word) + 1