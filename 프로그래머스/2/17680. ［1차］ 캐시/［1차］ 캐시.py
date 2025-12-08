def solution(cacheSize, cities):
    cache = []
    answer = 0
    
    processed_cities = [city.lower() for city in cities]
    
    for city in processed_cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.insert(0, city)
        else:
            answer += 5
            cache.insert(0, city)
        if len(cache) > cacheSize:
            cache.pop()
    return answer