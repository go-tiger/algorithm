function solution(dirs) {
    const directionMap = {
        U: [0, 1],
        D: [0, -1],
        R: [1, 0],
        L: [-1, 0]
    }

    const visitedPaths = new Set()
    let currentPosition = [0, 0]

    for (const dir of dirs) {
        const [dx, dy] = directionMap[dir]
        const nextX = currentPosition[0] + dx
        const nextY = currentPosition[1] + dy

        if (nextX < -5 || nextX > 5 || nextY < -5 || nextY > 5) {
            continue
        }

        const pathStart = [currentPosition[0], currentPosition[1]]
        const pathEnd = [nextX, nextY]

        const normalizedPath = currentPosition[0] < nextX || (currentPosition[0] === nextX && currentPosition[1] < nextY)
            ? `${pathStart[0]},${pathStart[1]}-${pathEnd[0]},${pathEnd[1]}`
            : `${pathEnd[0]},${pathEnd[1]}-${pathStart[0]},${pathStart[1]}`
            
        visitedPaths.add(normalizedPath)
        currentPosition = [nextX, nextY]
    }
    return visitedPaths.size
}