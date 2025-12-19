function solution(maps) {
    let result = 0
    const visited = Array(maps.length).fill(0).map(()=> Array(maps[0].length).fill(0))
    const dy = [1, 0, -1, 0]
    const dx = [0, 1, 0, -1]
    const q = []
    q.push([0, 0])
    visited[0][0] = 1
    
    if (maps[maps.length - 1][maps[0].length - 2] === 0 && maps[maps.length - 2][maps[0].length - 1] === 0) return -1
    
    while (q.length) {
       const [y, x] = q.shift()
        
        for (let i = 0; i < 4; i++) {
            let ny = y + dy[i]
            let nx = x + dx[i]
            
            if (ny < 0 || nx < 0 || ny >= maps.length || nx >= maps[0].length || maps[ny][nx] === 0 ) continue
            if (visited[ny][nx]) continue
            q.push([ny, nx])
            visited[ny][nx] = visited[y][x] + 1
        }
    }
    
    result = visited[maps.length - 1][maps[0].length - 1]
    
    if(!result) return -1
    return result
}