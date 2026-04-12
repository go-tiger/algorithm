def solution(lines):
    arr = []
    cnt = {}
    s = set()
    
    for x, y in lines:
        for i in range(x, y):
            key = str(i) + str(i+1)
            arr.append(key)
    
    for v in arr:
        cnt[v] = cnt.get(v, 0) + 1
    
    for v in arr:
        if cnt[v] != 1:
            s.add(v)
    
    return len(s)