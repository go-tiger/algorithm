function solution(word) {
	const dictionary = [];
	const vowels = ["A", "E", "I", "O", "U"];
    
	function generateWords(currentWord) {
		if (currentWord.length === 5) {
			return;
		}
        
		for (let i = 0; i < vowels.length; i++) {
			const newWord = currentWord + vowels[i];
			dictionary.push(newWord);
			generateWords(newWord);
		}
	}
	generateWords("");
	return dictionary.indexOf(word) + 1;
}