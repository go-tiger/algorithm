function solution(n, computers) {
    let networks = 0
    let visit = Array(n).fill(false)

    for (let i = 0; i < n; i++) {
        if (!visit[i]) {
            networks ++
            isVisit(i)
        }
    }
    
    function isVisit(index) {
        visit[index] = true
        
        const computer = computers[index]
        
        for (let i = 0; i < computer.length; i++) {
            const isConnect = computer[i] === 1 ? true : false;

            if (!visit[i] && isConnect) {
                isVisit(i)
            }
        }        
    }
    return networks
}