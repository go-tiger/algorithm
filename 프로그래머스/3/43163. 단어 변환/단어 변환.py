def solution(begin, target, words):
    answer = [51]

    def check_next_word(cur, nxt):
        diff_count = sum(1 for c, n in zip(cur, nxt) if c != n)
        return diff_count == 1

    def search_words(cur_word, visited, count):
        if cur_word == target:
            answer[0] = min(answer[0], count)
            return

        for i, word in enumerate(words):
            if not visited[i] and check_next_word(cur_word, word):
                visited[i] = True
                search_words(word, visited, count + 1)
                visited[i] = False

    if target in words:
        search_words(begin, [False] * len(words), 0)

    return 0 if answer[0] == 51 else answer[0]