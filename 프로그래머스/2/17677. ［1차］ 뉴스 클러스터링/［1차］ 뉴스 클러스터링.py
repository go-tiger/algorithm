def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    arr1 = []
    arr2 = []
    
    for i in range(len(str1) - 1):
        s = str1[i:i+2]
        if s[0].isalpha() and s[1].isalpha():
            arr1.append(s)
            
    for i in range(len(str2) - 1):
        s = str2[i:i+2]
        if s[0].isalpha() and s[1].isalpha():
            arr2.append(s)

    intersection = []
    
    temp_arr1 = list(arr1)
    union_elements = [] 
    
    for item2 in arr2:
        if item2 in temp_arr1:
            intersection.append(item2)
            temp_arr1.remove(item2)
        union_elements.append(item2)

    for item1 in temp_arr1:
        union_elements.append(item1)
    
    len_intersection = len(intersection)
    len_union = len(union_elements)

    if len_intersection == 0 and len_union == 0:
        return 65536
        
    if len_union == 0:
        return 0
    
    return int(65536 * (len_intersection / len_union))