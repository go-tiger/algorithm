def solution(name, yearning, photo):
    name_yearning_map = {n: y for n, y in zip(name, yearning)}
    result = []
    
    for single_photo_row in photo:
        current_sum = 0
        for person_in_photo in single_photo_row:
            current_sum += name_yearning_map.get(person_in_photo, 0)
        result.append(current_sum)
        
    return result