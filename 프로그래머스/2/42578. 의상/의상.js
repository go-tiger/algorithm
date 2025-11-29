function solution(clothes) {
  const typeCounts = {}
  
  clothes.forEach(item => {
    const type = item[1]
    typeCounts[type] = (typeCounts[type] || 0) + 1
  });
  
  let totalCombinations = 1
    
  for (let type in typeCounts) {
    totalCombinations *= (typeCounts[type] + 1)
  }
  
  return totalCombinations - 1
}