function solution(elements) {
    const inbox = new Set()
    for (i = 1; i <= elements.length; i++) {
        const newElements = elements.concat(elements.slice(0, i));
         for (k = 0; k < elements.length; k++) {
             inbox.add(newElements.slice(k, k + i).reduce((a, b) => a + b))
         }
    }
    return inbox.size
}