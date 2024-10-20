function solution(sizes) {
    let w = []
    let h = []
    
    sizes.map((v,i) => {
      w[i] = Math.max(...v)
      h[i] = Math.min(...v)
    })

    return Math.max(...w) * Math.max(...h)
}