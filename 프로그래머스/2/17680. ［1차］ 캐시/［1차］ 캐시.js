function solution(cacheSize, cities) {
    let cache = []
    let answer = 0
    cities = cities.map((city) => city.toLowerCase())
    
    for (let i=0; i<cities.length; i++) {
        if (cache.includes(cities[i])) {
            answer += 1
            cache.splice(cache.indexOf(cities[i]), 1)
            cache.unshift(cities[i])
        } else {
            answer += 5
            cache.unshift(cities[i])
        }
        
        if (cache.length > cacheSize) {
            cache.pop()
        }
    }
    return answer;
}